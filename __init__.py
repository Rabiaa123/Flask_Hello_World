from flask import Flask
from flask import render_template
from flask import json
from flask import Flask, request
import sqlite3
                                                                                                                                       
app = Flask(__name__)     

@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html') 
  
@app.route('/vallet/')
def exercices_svg():
    return render_template('svg-cards.html') 
  
@app.route('/TP1/')
def exercices_tp1():
    return render_template('page1.html') 

@app.route('/maison/')
def exercices_forme():
    return render_template('Exemple_Base_SVG.html') 
  
@app.route('/formulaire/')
def exercice4():
    return render_template('formulaire.html') 

@app.route('/exercice_base1/')
def exercice1():
    return render_template('1_Liste_Base.html')

@app.route('/exercice_base2/')
def exercice2():
    return render_template('2_Liste_Base.html')

@app.route('/exercice_base3/')
def exercice3():
    return render_template('3_Liste_Base.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route("/cnam/")
def MaPremiereAPI1():
    return render_template("cnam.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    result = valeur1 + valeur2
    return f"<h2>La somme de {valeur1} et {valeur2} est : {result}</h2>"

@app.route('/addition/<valeurs>')
def addition(valeurs):
    try:
        nombres = list(map(int, valeurs.split(',')))
        resultat = sum(nombres)
        return f"<h2>La somme des valeurs {nombres} est : {resultat}</h2>"
    except ValueError:
        return "<h2>Erreur : Assurez-vous d'entrer uniquement des nombres séparés par des virgules.</h2>"

@app.route('/somme_pair_impaire/<int:valeur1>/<int:valeur2>')
def somme2(valeur1, valeur2):
    resultat = valeur1 + valeur2
    pair_ou_impair = "pair" if resultat % 2 == 0 else "impair"
    return f"<h2>La somme de {valeur1} et {valeur2} est : {resultat} ({pair_ou_impair})</h2>"

@app.route('/max', methods=['GET', 'POST'])
def max_value():
    if request.method == 'POST':
        valeurs = request.form.get('valeurs')
        try:
            nombres = list(map(int, valeurs.split(',')))
            max_valeur = nombres[0]  # On suppose que le premier nombre est le plus grand
            for nombre in nombres:
                if nombre > max_valeur:
                    max_valeur = nombre
            return f"<h2>La valeur maximale parmi {nombres} est : {max_valeur}</h2>"
        except ValueError:
            return "<h2>Erreur : Veuillez entrer uniquement des nombres séparés par des virgules.</h2>"
    return '''
        <form method="post">
            <label>Entrez des nombres séparés par des virgules :</label>
            <input type="text" name="valeurs">
            <button type="submit">Trouver la valeur maximale</button>
        </form>
    '''
@app.route('/cv')
def cv():
    return render_template('cv.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
