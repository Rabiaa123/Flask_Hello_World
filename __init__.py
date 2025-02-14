from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)     

@app.route("/cnam/")
def MaPremiereAPI1():
    return render_template("cnam.html")
  
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return f"<h2>Le carré de votre valeur est :</h2> {escape(val_user * val_user)}"
  
@app.route('/exercices/')
def exercices():
    return render_template('exercices.html') #Commentaire

@app.route('/somme/<valeurs>')
def somme(valeurs):
    try:
        nombres = list(map(int, valeurs.split(',')))
        resultat = sum(nombres)
        return f"<h2>La somme des valeurs {nombres} est : {resultat}</h2>"
    except ValueError:
        return "<h2>Erreur : Assurez-vous d'entrer uniquement des nombres séparés par des virgules.</h2>"
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
