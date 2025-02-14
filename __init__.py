from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)     
  
@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)
  
@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    return f"<h2>La somme de {valeur1} et {valeur2} est : {valeur1 + valeur2}</h2>"

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    resultat = valeur1 + valeur2
    pair_ou_impair = "pair" if resultat % 2 == 0 else "impair"
    return f"<h2>La somme de {valeur1} et {valeur2} est : {resultat} ({pair_ou_impair})</h2>"
  
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")
  
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html') #Commentaire
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
