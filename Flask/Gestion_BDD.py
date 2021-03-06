#! /usr/bin/python
# -*- coding:utf-8 -*-


import sqlite3 as sql

def Insertion_Utilisateur(Nom, Prenom, Password, Email):
    connexion = sql.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Utilisateur (Nom, Prenom, Pass, Email, Admin) VALUES ('{}','{}','{}','{}','FALSE')".format(Nom, Prenom, Password, Email))
    connexion.commit()
    connexion.close()

def Recuperation_Utilisateur():
    connexion = sql.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Nom, Prenom, Pass, Email, Admin FROM Utilisateur")
    Utilisateurs = curseur.fetchall()
    connexion.close()
    return Utilisateurs

def Recuperation_Utilisateur_Specifique(Email_Utilisateur):
    connexion = sql.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Nom, Prenom, Pass, Email,Admin FROM Utilisateur WHERE Email = '{}'".format(Email_Utilisateur))
    Resultat = curseur.fetchone()
    connexion.close()
    return Resultat


def Recuperation_Articles():
    connexion = sql.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Titre, Contenu FROM Articles")
    Utilisateurs = curseur.fetchall()
    connexion.close()
    return Utilisateurs

def Insertion_Article(Titre, Contenu):
    connexion = sql.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Articles (Titre, Contenu) VALUES ('{}','{}')".format(Titre, Contenu))
    connexion.commit()
    connexion.close()