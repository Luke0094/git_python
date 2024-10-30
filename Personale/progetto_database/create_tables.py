import pymysql
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

# Configurazione del database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'db': 'users_db'
}

# Definizione degli utenti iniziali
users = [
    {
       'username': 'admin',
       'password': 'admin123',
       'email': 'admin@example.com',
       'is_admin': True,
       'is_superadmin': False,
       'is_approved': True
   },
   {
       'username': 'superadmin',
       'password': 'super123',
       'email': 'superadmin@example.com',
       'is_admin': True,
       'is_superadmin': True,
       'is_approved': True
   },
    {
       'username': 'mario',
       'password': 'mario123',
       'email': 'mario@example.com',
       'is_admin': False,
       'is_superadmin': False,
       'is_approved': True
   },
   {
       'username': 'luigi',
       'password': 'luigi123',
       'email': 'luigi@example.com',
       'is_admin': False,
       'is_superadmin': False,
       'is_approved': True
   }
]

# Definizione degli eventi di esempio
events = [
    {
        'title': 'Riunione Team',
        'description': 'Riunione mensile per discussione progetti',
        'event_date': '2024-11-01',
        'event_time': '10:00:00',
        'created_by': 1  # ID dell'admin
    },
    {
        'title': 'Workshop Python',
        'description': 'Workshop introduttivo alla programmazione Python',
        'event_date': '2024-11-15',
        'event_time': '14:30:00',
        'created_by': 1
    },
    {
        'title': 'Evento Networking',
        'description': 'Evento di networking aziendale',
        'event_date': '2024-11-30',
        'event_time': '18:00:00',
        'created_by': 1
    }
]

try:
    # Connessione al database
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    # Ricrea il database
    cursor.execute("DROP DATABASE IF EXISTS users_db")
    cursor.execute("CREATE DATABASE users_db")
    cursor.execute("USE users_db")

    # Crea tabella utenti
    cursor.execute("""
CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        is_admin BOOLEAN DEFAULT FALSE,
        is_superadmin BOOLEAN DEFAULT FALSE,
        is_approved BOOLEAN DEFAULT FALSE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """)

    # Inserisce gli utenti
    for user in users:
        hashed_password = generate_password_hash(user['password'])
        cursor.execute("""
        INSERT INTO users (username, password, email, is_admin, is_superadmin, is_approved)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (
       user['username'], 
       hashed_password, 
       user['email'],
       user['is_admin'],
       user['is_superadmin'],
       user['is_approved']
   ))

    # Crea tabella eventi
    cursor.execute("""
    CREATE TABLE events (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        event_date DATE NOT NULL,
        event_time TIME NOT NULL,
        created_by INT NOT NULL,
        FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """)

    # Crea tabella partecipazioni eventi
    cursor.execute("""
    CREATE TABLE event_participants (
        event_id INT,
        user_id INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (event_id, user_id),
        FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """)

    # Inserisce gli eventi
    for event in events:
        cursor.execute("""
        INSERT INTO events (title, description, event_date, event_time, created_by)
        VALUES (%s, %s, %s, %s, %s)
        """, (
            event['title'],
            event['description'],
            event['event_date'],
            event['event_time'],
            event['created_by']
        ))

    # Aggiunge alcune partecipazioni di esempio
    cursor.execute("""
    INSERT INTO event_participants (event_id, user_id)
    VALUES 
        (1, 2),  -- superadmin partecipa al primo evento
        (1, 3),  -- mario partecipa al primo evento
        (2, 3),  -- mario partecipa al secondo evento
        (2, 4)   -- luigi partecipa al secondo evento
    """)

    conn.commit()
    print("Database inizializzato con successo!")

    # Verifica i dati inseriti
    print("\nUtenti creati:")
    cursor.execute("SELECT id, username, email, is_admin, is_superadmin, is_approved FROM users")
    for user in cursor.fetchall():
        print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, " \
              f"Admin: {'Sì' if user[3] else 'No'}, " \
              f"SuperAdmin: {'Sì' if user[4] else 'No'}, " \
              f"Approvato: {'Sì' if user[5] else 'No'}")

    print("\nEventi creati:")
    cursor.execute("SELECT id, title, event_date, event_time FROM events")
    for event in cursor.fetchall():
        print(f"ID: {event[0]}, Titolo: {event[1]}, Data: {event[2]}, Ora: {event[3]}")

except Exception as e:
    print(f"Errore durante l'inizializzazione del database: {str(e)}")
    conn.rollback()

finally:
    cursor.close()
    conn.close()