drop table if exists Utilisateur;
create table Utilisateur (
    id integer primary key autoincrement,
    Nom text not null,
    Prenom text not null,
    Pass text not null,
    Email text not null,
    Admin boolean not null

);

create table Articles (
    id integer primary key autoincrement,
    Titre text not null,
    Contenu text not null
)