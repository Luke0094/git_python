from flask import Flask
from markupsafe import escape
from flask import url_for


app = Flask(__name__)

ciao = "prova"

def ciaobelli():
    return "Bella"

@app.route("/")
def hello_world():
    nome = "<script>console.log('puzzi')</script>"
    return f"<h2>{ciao}{ciaobelli()} {escape(nome)}!</h2><a href='{url_for('about_me')}'>about me</a><p>{url_for('about_me')}</p>"

@app.route("/beppe")
@app.route("/about")
@app.route("/studenti/prof")
def about_me():
    return f"<p>Ciao sono Mattia e mi piace Flask</p><a href='{url_for('hello_world')}'>about me</a>"

@app.route('/studenti/<username>')
def show_user_profile(username):
    # carico informazioni sul db
    return f'User {escape(username)}'