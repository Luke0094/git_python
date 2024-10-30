-- avvia tramite terminale
(in caso di errore prima
Set-ExecutionPolicy Unrestricted -Force)
python -m venv .venv

--a avvia tramite terminale
.venv\Scripts\activate 

--installa le dipendenze da terminale
pip install -r requirements.txt

-- tramite terminale apri con
python app.py


aggiungere il db con la query in mariaDB

per settare gli utenti e eventi inizialmente
python create_tables.py