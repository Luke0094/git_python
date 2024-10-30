// main.js

document.addEventListener('DOMContentLoaded', function() {
    // Gestione form di registrazione
    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch('/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                const result = await response.json();
                if (result.success) {
                    alert(result.message);
                    window.location.reload();
                } else {
                    alert(result.message);
                }
            } catch (error) {
                alert('Errore durante la registrazione');
            }
        });
    }

    // Gestione form di login
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                const result = await response.json();
                if (result.success) {
                    window.location.reload();
                } else {
                    alert(result.message);
                }
            } catch (error) {
                alert('Errore durante il login');
            }
        });
    }

    // Gestione form eventi
    const addEventForm = document.getElementById('addEventForm');
    if (addEventForm) {
        addEventForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch('/add_event', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                const result = await response.json();
                if (result.success) {
                    window.location.reload();
                } else {
                    alert(result.message);
                }
            } catch (error) {
                alert('Errore durante l\'aggiunta dell\'evento');
            }
        });
    }
});

// Funzione per partecipare a un evento
function participate(eventId) {
    fetch(`/participate/${eventId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            window.location.reload();
        } else {
            alert(result.message);
        }
    })
    .catch(() => {
        alert('Errore durante la partecipazione all\'evento');
    });
}

function showParticipants(eventId) {
    fetch(`/admin/event_participants/${eventId}`)
        .then(response => response.json())
        .then(participants => {
            alert('Partecipanti:\n' + participants.join('\n'));
        });
}

// Funzione per cancellare la partecipazione
function cancelParticipation(eventId) {
    fetch(`/cancel_participation/${eventId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            window.location.reload();
        } else {
            alert(result.message);
        }
    })
    .catch(() => {
        alert('Errore durante la cancellazione della partecipazione');
    });
}

// Funzione per eliminare un utente
function deleteUser(userId) {
    if (!confirm('Sei sicuro di voler eliminare questo utente?')) {
        return;
    }

    fetch(`/delete_user/${userId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(result => {
        alert(result.message);
        if (result.success) {
            loadUsers();
        }
    })
    .catch(error => {
        alert('Errore durante l\'eliminazione dell\'utente');
        console.error('Errore:', error);
    });
}
 
function toggleApproval(userId) {
    fetch(`/admin/toggle_approval/${userId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            window.location.reload();
        }
    })
    .catch(error => {
        console.error('Errore:', error);
        alert('Errore durante l\'operazione');
    });
}

function toggleAdminStatus(userId) {
    fetch(`/admin/toggle_status/${userId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            window.location.reload();
        }
    })
    .catch(error => {
        console.error('Errore:', error);
        alert('Errore durante l\'operazione');
    });
}
// Funzione per caricare gli utenti
async function loadUsers() {
    try {
        const response = await fetch('/users');
        const users = await response.json();
        const tbody = document.getElementById('usersTable');
        if (tbody) {
            tbody.innerHTML = users.map(user => `
                <tr>
                    <td>${user.id}</td>
                    <td>${user.username}</td>
                    <td>${user.email}</td>
                    <td>${user.is_admin ? 'Sì' : 'No'}</td>
                    <td>
                        <button class="btn ${user.is_admin ? 'btn-warning' : 'btn-primary'} btn-sm me-2" 
                                onclick="toggleAdminStatus(${user.id})">
                            ${user.is_admin ? 'Rimuovi Admin' : 'Promuovi Admin'}
                        </button>
                        <button class="btn ${user.is_approved ? 'btn-danger' : 'btn-success'} btn-sm me-2" 
                                onclick="toggleApproval(${user.id})">
                            ${user.is_approved ? 'Revoca Approvazione' : 'Approva'}
                        </button>
                    </td>
                </tr>
            `).join('');
        }
    } catch (error) {
        console.error('Errore:', error);
        alert('Errore nel caricamento degli utenti');
    }
}

// Funzione per caricare gli eventi
function loadEvents() {
    fetch('/admin/events')
        .then(response => response.json())
        .then(events => {
            const tbody = document.getElementById('eventsTable');
            if (tbody) {
                tbody.innerHTML = '';
                events.forEach(event => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${event.id}</td>
                        <td>${event.title}</td>
                        <td>${event.event_date}</td>
                        <td>${event.event_time}</td>
                        <td>${event.participants_count}</td>
                        <td>
                            <button class="btn btn-danger btn-sm" onclick="deleteEvent(${event.id})">
                                Elimina
                            </button>
                        </td>
                    `;
                    tbody.appendChild(row);
                });
            }
        })
        .catch(error => {
            console.error('Errore nel caricamento degli eventi:', error);
        });
}

// Funzione per caricare le partecipazioni
function loadParticipations() {
    fetch('/admin/participations')
        .then(response => response.json())
        .then(participations => {
            const tbody = document.getElementById('participationsTable');
            if (tbody) {
                tbody.innerHTML = '';
                participations.forEach(p => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${p.event_title}</td>
                        <td>${p.event_date}</td>
                        <td>${p.username}</td>
                        <td>${p.created_at}</td>
                        <td>
                            <button class="btn btn-danger btn-sm" onclick="removeParticipation(${p.event_id}, ${p.user_id})">
                                Rimuovi
                            </button>
                        </td>
                    `;
                    tbody.appendChild(row);
                });
            }
        })
        .catch(error => {
            console.error('Errore nel caricamento delle partecipazioni:', error);
        });
}

// Funzione per eliminare un evento
function deleteEvent(eventId) {
    if (!confirm('Sei sicuro di voler eliminare questo evento?')) return;

    fetch(`/admin/delete_event/${eventId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            loadEvents();
        } else {
            alert(result.message);
        }
    })
    .catch(error => {
        console.error('Errore durante l\'eliminazione dell\'evento:', error);
    });
}

// Funzione per rimuovere una partecipazione
function removeParticipation(eventId, userId) {
    if (!confirm('Sei sicuro di voler rimuovere questa partecipazione?')) return;

    fetch(`/admin/remove_participation/${eventId}/${userId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            loadParticipations();
        } else {
            alert(result.message);
        }
    })
    .catch(error => {
        console.error('Errore durante la rimozione della partecipazione:', error);
    });
}

// Carica i dati quando si apre il pannello admin
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('adminTabs')) {
        loadUsers();
        loadEvents();
        loadParticipations();
    }
});