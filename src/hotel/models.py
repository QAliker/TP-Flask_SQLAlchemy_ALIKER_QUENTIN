# importer l'instanciation db de SQLAlchemy
from .database import db
from datetime import datetime

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