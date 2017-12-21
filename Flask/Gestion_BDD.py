import sqlite3 as sql

def Insertion_Utilisateur(Nom, Prenom, Password, Email):
    connexion = sql.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Utilisateur (Nom, Prenom, Pass, Email, Admin) VALUES (?,?,?,?,?)", (Nom, Prenom, Password, Email, 'False'))
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
