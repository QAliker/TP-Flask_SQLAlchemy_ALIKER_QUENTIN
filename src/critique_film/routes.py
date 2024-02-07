from flask import Blueprint, render_template
from .forms import InscriptionForm
from werkzeug.security import generate_password_hash
from .database import db
from .models import Utilisateur


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = InscriptionForm()
    # opérations pour enregistrer le formulaire
    if form.validate_on_submit():
        # enregistrer le formulaire
        # générer le hash du mot de passe
        hashed_password = generate_password_hash(form.mot_de_passe.data, salt_length=8)
        # enregistrer l'utilisateur
        new_user = Utilisateur(
            nom=form.nom.data,
            email=form.email.data,
            mot_de_passe_hash=hashed_password
        )

        # ajouter l'utilisateur dans la base de données
        # Enregistrer la modification
        db.session.add(new_user)

        # Appliquer les modifications
        db.session.commit()
        return render_template('index.html')
    return render_template('inscription.html', form=form)

@main.route('/ajouter-film', methods=['GET', 'POST'])
def ajouter_film():
    
