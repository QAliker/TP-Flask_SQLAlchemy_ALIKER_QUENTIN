# importer l'instanciation db de SQLAlchemy
from .database import db
from datetime import datetime

# class Utilisateur(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nom = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(80), unique=True, nullable=False)
#     mot_de_passe_hash = db.Column(db.String(500), nullable=False)
#     critiques= db.relationship('Critique', backref='utilisateur', lazy='dynamic')


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    realisateur = db.Column(db.String(100))
    annee_sortie = db.Column(db.Integer)
    genre = db.Column(db.String(100))
    # critiques = db.relationship('Critique', backref='film', lazy='dynamic')
class Critique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenu = db.Column(db.Text, nullable=False)
    date_post = db.Column(db.DateTime, default=datetime.utcnow)
    date_posts = db.Column(db.DateTime, default=datetime.utcnow)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))
    id_film = db.Column(db.Integer, db.ForeignKey('film.id'))
    film = db.relationship('Film', backref='critique', lazy=True)


class Auteur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    date_de_naissance = db.Column(db.DateTime, default=datetime.utcnow)
    country = db.Column(db.String(200))
    livres = db.relationship('Livre', backref='auteur', lazy=True)

class Livre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    date_de_publication = db.Column(db.DateTime, default=datetime.utcnow)
    genre = db.Column(db.String(100))
    id_auteur = db.Column(db.Integer, db.ForeignKey('auteur.id'))
    auteur_id = db.relationship('Auteur', backref='livre', lazy=True)
    emprunts = db.relationship('Emprunt', backref='livre', lazy=True)

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    emprunts = db.relationship('Emprunt', backref='utilisateur', lazy=True)

class Emprunt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)
    id_livre = db.Column(db.Integer, db.ForeignKey('livre.id'), nullable=False)
    date_emprunt = db.Column(db.DateTime, default=datetime.utcnow)
    date_retour = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    reservation = db.relationship('Reservation', backref='client', lazy=True)

class Chambre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, unique=True, nullable=False)
    type = db.Column(db.String(100), nullable=False) 
    prix = db.Column(db.Integer, nullable=False)
    reservation = db.relationship('Reservation', backref='chambre', lazy=True)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_client = db.Column(db.Integer, db.ForeignKey('client.id'))
    id_chambre = db.Column(db.Integer, db.ForeignKey('chambre.id'))
    date_arrivee = db.Column(db.DateTime, default=datetime.utcnow)
    date_depart = db.Column(db.DateTime, default=datetime.utcnow)
    statut = db.Column(db.String(100),)