from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)     
  
@app.route("/", methods=["GET", "POST"])
def max_value():
    max_val = None
    numbers = []

    if request.method == "POST":
        try:
            numbers = list(map(float, request.form.getlist("numbers")))
            if numbers:
                max_val = max(numbers)
        except ValueError:
            return "Veuillez entrer uniquement des nombres valides."

    return render_template("index.html", max_val=max_val, numbers=numbers)
  
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
