from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)     
  
@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/somme', methods=['GET', 'POST'])
def somme():
    if request.method == 'POST':
        valeurs = request.form.get('valeurs')
        try:
            # Convertir la saisie en une liste d'entiers
            nombres = list(map(int, valeurs.split(',')))
            
            # Calculer la somme avec une boucle
            total = 0
            for nombre in nombres:
                total += nombre
            
            return f"<h2>La somme des valeurs {nombres} est : {total}</h2>"
        except ValueError:
            return "<h2>Erreur : Veuillez entrer uniquement des nombres séparés par des virgules.</h2>"

    # Afficher le formulaire
    return '''
        <form method="post">
            <label>Entrez des nombres séparés par des virgules :</label>
            <input type="text" name="valeurs">
            <button type="submit">Calculer</button>
        </form>
    '''

  
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
