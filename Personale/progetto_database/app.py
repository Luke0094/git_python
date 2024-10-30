import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, render_template, request, jsonify, flash, session, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Configurazione MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'users_db'

mysql = MySQL(app)

@app.route('/')
def index():
    events = []
    if session.get('logged_in'):
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT e.*, 
                   CASE WHEN ep.user_id IS NOT NULL THEN 1 ELSE 0 END as is_participant,
                   COUNT(DISTINCT ep2.user_id) as participants_count
            FROM events e
            LEFT JOIN event_participants ep ON e.id = ep.event_id 
                AND ep.user_id = %s
            LEFT JOIN event_participants ep2 ON e.id = ep2.event_id
            GROUP BY e.id
            ORDER BY e.event_date, e.event_time
        """, (session.get('user_id'),))
        events_data = cur.fetchall()
        cur.close()
        
        for event in events_data:
            event_time = event[4]
            if isinstance(event_time, timedelta):
                hours = int(event_time.total_seconds() // 3600)
                minutes = int((event_time.total_seconds() % 3600) // 60)
                time_str = f"{hours:02d}:{minutes:02d}"
            else:
                time_str = event_time.strftime('%H:%M') if event_time else ''

            events.append({
                'id': event[0],
                'title': event[1],
                'description': event[2],
                'event_date': event[3].strftime('%d/%m/%Y') if event[3] else '',
                'event_time': time_str,
                'is_participant': bool(event[6]),
                'participants_count': event[7]
            })
    
    return render_template('index.html', events=events)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            
            if not username or not password or not email:
                return jsonify({'success': False, 'message': 'Tutti i campi sono obbligatori'})

            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (username, password, email, is_admin) VALUES (%s, %s, %s, %s)",
                       (username, hashed_password, email, False))
            mysql.connection.commit()
            cur.close()
            
            return jsonify({'success': True, 'message': 'Registrazione completata con successo'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            cur.close()
            
            if not user:
                return jsonify({'success': False, 'message': 'Credenziali non valide'})
            
            if not user[6] and not user[5]:  # not approved and not superadmin
                return jsonify({'success': False, 'message': 'Account in attesa di approvazione'})
                
            if user and check_password_hash(user[2], password):
                session['logged_in'] = True
                session['username'] = username
                session['user_id'] = user[0]
                session['is_admin'] = user[4]
                session['is_superadmin'] = user[5]
                return jsonify({'success': True, 'is_admin': user[4], 'message': 'Login effettuato'})
            
            return jsonify({'success': False, 'message': 'Credenziali non valide'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
    return redirect(url_for('index'))

@app.route('/admin')
def admin_panel():
    if not session.get('logged_in') or not session.get('is_admin'):
        return jsonify({'success': False, 'message': 'Accesso non autorizzato'})
    
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, username, email, is_admin FROM users")
        users = cur.fetchall()
        cur.close()
        return render_template('admin.html', users=users)
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})
    
@app.route('/toggle_user_approval/<int:id>', methods=['POST'])
def toggle_user_approval(id):
   if not session.get('is_admin'):
       return jsonify({'success': False})
   try:
       cur = mysql.connection.cursor()
       cur.execute("UPDATE users SET is_approved = NOT is_approved WHERE id = %s", (id,))
       mysql.connection.commit()
       cur.close()
       return jsonify({'success': True})
   except:
       return jsonify({'success': False})

@app.route('/admin/toggle_status/<int:id>', methods=['POST'])
def toggle_admin_status(id):
    if not session.get('is_superadmin'):
        return jsonify({'success': False, 'message': 'Non autorizzato'})
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT is_superadmin FROM users WHERE id = %s", (id,))
        user = cur.fetchone()
        if user and user[0]:
            return jsonify({'success': False, 'message': 'Non puoi modificare un superadmin'})
        
        cur.execute("UPDATE users SET is_admin = NOT is_admin WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/admin/toggle_approval/<int:id>', methods=['POST'])
def toggle_approval(id):
    if not session.get('is_admin') and not session.get('is_superadmin'):
        return jsonify({'success': False, 'message': 'Non autorizzato'})
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT is_superadmin FROM users WHERE id = %s", (id,))
        user = cur.fetchone()
        if user and user[0]:
            return jsonify({'success': False, 'message': 'Non puoi modificare un superadmin'})
            
        cur.execute("UPDATE users SET is_approved = NOT is_approved WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/users')
def get_users():
    if not session.get('logged_in') or not session.get('is_admin'):
        return jsonify({'success': False, 'message': 'Accesso non autorizzato'})
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, username, email, is_admin, is_superadmin, is_approved FROM users")
        users = cur.fetchall()
        cur.close()
        
        users_list = []
        for user in users:
            users_list.append({
                'id': user[0],
                'username': user[1],
                'email': user[2],
                'is_admin': user[3],
                'is_superadmin': user[4],
                'is_approved': user[5]
            })
        return jsonify(users_list)
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/admin/events')
def admin_events():
    if not session.get('logged_in') or not session.get('is_admin'):
        return jsonify({'success': False, 'message': 'Accesso non autorizzato'})
    
    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT e.*, COUNT(ep.user_id) as participants_count 
            FROM events e 
            LEFT JOIN event_participants ep ON e.id = ep.event_id 
            GROUP BY e.id
            """)
        events = cur.fetchall()
        cur.close()
        
        events_list = []
        for event in events:
            event_time = event[4]
            if isinstance(event_time, timedelta):
                hours = int(event_time.total_seconds() // 3600)
                minutes = int((event_time.total_seconds() % 3600) // 60)
                time_str = f"{hours:02d}:{minutes:02d}"
            else:
                time_str = event_time.strftime('%H:%M') if event_time else ''

            events_list.append({
                'id': event[0],
                'title': event[1],
                'description': event[2],
                'event_date': event[3].strftime('%d/%m/%Y'),
                'event_time': time_str,
                'participants_count': event[5]
            })
        
        return jsonify(events_list)
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/admin/participations')
def admin_participations():
    if not session.get('logged_in') or not session.get('is_admin'):
        return jsonify({'success': False, 'message': 'Accesso non autorizzato'})
    
    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT e.title, e.event_date, u.username, ep.created_at, e.id, u.id
            FROM event_participants ep
            JOIN events e ON ep.event_id = e.id
            JOIN users u ON ep.user_id = u.id
            ORDER BY e.event_date, e.title, u.username
            """)
        participations = cur.fetchall()
        cur.close()
        
        participations_list = []
        for p in participations:
            participations_list.append({
                'event_title': p[0],
                'event_date': p[1].strftime('%d/%m/%Y'),
                'username': p[2],
                'created_at': p[3].strftime('%d/%m/%Y %H:%M'),
                'event_id': p[4],
                'user_id': p[5]
            })
        
        return jsonify(participations_list)
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/delete_user/<int:id>', methods=['POST'])
def delete_user(id):
    if not session.get('logged_in') or not session.get('is_admin'):
        return jsonify({'success': False, 'message': 'Accesso non autorizzato'})
    
    try:
        # Verifica che l'utente non stia cercando di eliminare se stesso
        if id == session.get('user_id'):
            return jsonify({'success': False, 'message': 'Non puoi eliminare il tuo account'})

        # Recupera informazioni sull'utente da eliminare
        cur = mysql.connection.cursor()
        cur.execute("SELECT username, is_admin FROM users WHERE id = %s", (id,))
        user_to_delete = cur.fetchone()

        if not user_to_delete:
            cur.close()
            return jsonify({'success': False, 'message': 'Utente non trovato'})

        # Verifica se l'utente da eliminare è un superadmin
        if user_to_delete[1] and user_to_delete[0] == 'superadmin':
            cur.close()
            return jsonify({'success': False, 'message': 'Non puoi eliminare il superadmin'})

        # Procedi con l'eliminazione
        cur.execute("DELETE FROM users WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'success': True, 'message': 'Utente eliminato con successo'})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/admin/remove_participation/<int:event_id>/<int:user_id>', methods=['POST'])
def admin_remove_participation(event_id, user_id):
    if not session.get('logged_in') or not session.get('is_admin'):
        return jsonify({'success': False, 'message': 'Accesso non autorizzato'})
    
    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            DELETE FROM event_participants 
            WHERE event_id = %s AND user_id = %s
            """, (event_id, user_id))
        mysql.connection.commit()
        cur.close()
        return jsonify({'success': True, 'message': 'Partecipazione rimossa con successo'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/participate/<int:event_id>', methods=['POST'])
def participate(event_id):
    if not session.get('logged_in'):
        return jsonify({'success': False, 'message': 'Devi effettuare il login'})
    
    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO event_participants (event_id, user_id)
            VALUES (%s, %s)
            """, (event_id, session.get('user_id')))
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'success': True, 'message': 'Partecipazione registrata'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/cancel_participation/<int:event_id>', methods=['POST'])
def cancel_participation(event_id):
    if not session.get('logged_in'):
        return jsonify({'success': False, 'message': 'Devi effettuare il login'})
    
    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            DELETE FROM event_participants 
            WHERE event_id = %s AND user_id = %s
            """, (event_id, session.get('user_id')))
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'success': True, 'message': 'Partecipazione cancellata'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/add_event', methods=['POST'])
def add_event():
    if not session.get('logged_in') or not session.get('is_admin'):
        return jsonify({'success': False, 'message': 'Accesso non autorizzato'})
    
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        date = data.get('date')
        time = data.get('time')
        
        # Converti la stringa dell'ora in un oggetto time
        try:
            event_time = datetime.strptime(time, '%H:%M').time()
        except ValueError:
            return jsonify({'success': False, 'message': 'Formato ora non valido'})
        
        # Converti la stringa della data in un oggetto date
        try:
            event_date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'success': False, 'message': 'Formato data non valido'})
        
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO events (title, description, event_date, event_time, created_by)
            VALUES (%s, %s, %s, %s, %s)
            """, (title, description, event_date, event_time, session.get('user_id')))
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'success': True, 'message': 'Evento aggiunto con successo'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)