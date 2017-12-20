#! /usr/bin/python
# -*- coding:utf-8 -*-

import os
import sqlite3
from flask import *
import Gestion_BDD
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
    Gestion_BDD.Insertion_Utilisateur(Nom, Prenom, Password, Email)
    return "Nom : {}\nPrenom: {}\nEmail: {}\nPassword: {}".format(Nom, Prenom, Email, Password)
    
@app.route("/debug", methods=['GET'])
def debug():
    AllUtilisateurs = Gestion_BDD.Recuperation_Utilisateur()
    return AllUtilisateurs[0][0]

if __name__ == '__main__':
    app.run(debug=True)