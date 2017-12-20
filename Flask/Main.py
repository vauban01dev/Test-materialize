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
    return render_template('debug.html', AllUtilisateurs=AllUtilisateurs)

@app.route("/connexion", methods=['GET'])
def connexion_form():
    return render_template('Connexion.html')

@app.route("/connexion", methods=['POST'])
def connexion_traitement():
    UtilisateurBDD = Gestion_BDD.Recuperation_Utilisateur_Specifique(request.form['Email'])
    if UtilisateurBDD is None:
        return "Pas d'utilisateur en base"
    else:
        if request.form['Password'] == UtilisateurBDD[2]:
            session['Email'] = UtilisateurBDD[3]
            session['Nom'] = UtilisateurBDD[0]
            session['Prenom'] = UtilisateurBDD[1]         
            return session['Email']
        else:
            return "erreur de mot de passe"




if __name__ == '__main__':
    app.secret_key = '1234'

    app.run(debug=True)
    