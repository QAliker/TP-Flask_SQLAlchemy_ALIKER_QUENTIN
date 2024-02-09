import datetime
from flask import Blueprint, render_template
from .forms import InscriptionForm, AjoutFilmForm, CritiqueForm
from werkzeug.security import generate_password_hash
from .database import db
from .models import Utilisateur, Film, Critique, Auteur, Livre, Chambre, Reservation
from flask import jsonify
from flask import request
from sqlalchemy import and_



main = Blueprint('main', __name__)

@main.route('/api/chambres', methods=['POST'])
def addRoom():
        data = request.json
        numero = data.get('numero')
        type = data.get('type')
        prix = data.get('prix')
        chambre = Chambre(numero = numero, type=type, prix=prix )
        db.session.add(chambre)
        db.session.commit()

        return jsonify({'sucess': True, 'message': 'Chambre ajoutée avec succès.'})
@main.route('/api/chambres/<int:id>', methods=['PUT'])
def ChangeRoom(id):
    room = Chambre.query.get_or_404(id)
    data = request.json
    numero = data.get('numero')
    type = data.get('type')
    prix = data.get('prix')
    if room:
        room.numero = numero
        room.type = type
        room.prix = prix
        db.session.commit()
        return jsonify({'success': True, 'message': "Chambre mise à jour avec succès."})
    else:
        return jsonify({'success': False, 'message': "Chambre avec l id donné n existe pas."})

@main.route('/api/chambres/<int:id>', methods=['DELETE'])
def deleteRoom(id):
    chambre = Chambre.query.get_or_404(id)  
    if chambre:  
        db.session.delete(chambre) 
        db.session.commit()
        return jsonify({'success': True, "message": "Chambre supprimée avec succès."})
    else:
        return jsonify({'success': False, "message": "Chambre avec l'id donné n'existe pas."})

@main.route('/api/reservations', methods=['POST'])
def createReservation():
    reservation = Reservation.query.all()
    data = request.json
    id_client = data.get('id_client')
    id_chambre = data.get('id_chambre')
    date_depart = data.get('date_depart')
    date_arrivee = data.get('date_arrivee')
    if isRoomAvailable(id_chambre, date_depart, date_arrivee):
        reservation = Reservation(id_client=id_client, id_chambre=id_chambre, date_depart=date_depart, date_arrivee=date_arrivee)
        db.session.add(reservation)
        db.session.commit()
        return jsonify({'sucess': True, "message": "Chambre ajoutée avec succès."})
    else:
        return jsonify({'success': False, "message": "La chambre demandée n'est pas disponible pour les dates spécifiées."})

def isRoomAvailable(id_chambre, date_depart, date_arrivee):
    existing_reservations = Reservation.query.filter(
        (Reservation.id_chambre == id_chambre) and (
            Reservation.date_depart <= date_arrivee,
            Reservation.date_arrivee >= date_depart
        )
    ).all()

    return len(existing_reservations) == 0

@main.route('/api/reservations/<int:id>', methods=['DELETE'])
def deleteReservation(id):
    reservation = Reservation.query.get_or_404(id)  
    if reservation:  
        db.session.delete(reservation) 
        db.session.commit()
        return jsonify({'success': True, "message": "Reservation supprimée avec succès."})
    else:
        return jsonify({'success': False, "message": "Reservation avec l'id donné n'existe pas."})

@main.route('/api/chambres/disponibles', methods=['GET'])
def getAvailableRooms():
    data = request.json
    date_depart = data.get('date_depart')
    date_arrivee = data.get('date_arrivee')

    available_rooms = []

    chambres = Chambre.query.all()
    for chambre in chambres:
        if isRoomAvailable(chambre.id, date_depart, date_arrivee):
            available_rooms.append({
                'id': chambre.id,
                'numero': chambre.numero,
                'type': chambre.type,
                'prix': chambre.prix
            })

    return jsonify(available_rooms)
