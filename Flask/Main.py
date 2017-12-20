#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import *
app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template('Squelette.html')


@app.route("/inscription", methods=['GET'])
def inscription_form():
    return render_template('Inscription.html')

@app.route("/inscription", methods=['POST'])
def inscription_traitement():
    Nom = request.form['Nom']
    Prenom = request.form['Prenom']
    Email = request.form['Email']
    Password = request.form['Password']
    return "Nom : {}\nPrenom: {}\nEmail: {}\nPassword: {}".format(Nom, Prenom, Email, Password)
    


if __name__ == '__main__':
    app.run(debug=True)