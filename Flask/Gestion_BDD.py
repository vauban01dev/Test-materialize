import sqlite3 as sql

def Insertion_Utilisateur(Nom, Prenom, Password, Email):
    connexion = sql.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Utilisateur (Nom, Prenom, Pass, Email) VALUES (?,?,?,?)", (Nom, Prenom, Password, Email))
    connexion.commit()
    connexion.close()

def Recuperation_Utilisateur():
    connexion = sql.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Nom, Prenom, Pass, Email FROM Utilisateur")
    Utilisateurs = curseur.fetchall()
    connexion.close()
    return Utilisateurs