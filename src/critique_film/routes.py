import datetime
from flask import Blueprint, render_template
from .forms import InscriptionForm, AjoutFilmForm, CritiqueForm
from werkzeug.security import generate_password_hash
from .database import db
from .models import Utilisateur, Film, Critique, Auteur, Livre


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



@main.route('/films')
def films():
    films = Film.query.all()
    return render_template('films.html', films=films)

@main.route('/film/<int:id>')
def film_detail(id):
    film = Film.query.get_or_404(id)
    return render_template('film_detail.html', film=film)

@main.route('/ajouter-film', methods=['GET', 'POST'])
def ajouter_film():
    form = AjoutFilmForm()
    if form.validate_on_submit():
        new_film = Film(
            titre=form.titre.data,
            realisateur=form.realisateur.data,
            annee_sortie=form.annee_sortie.data,
            genre=form.genre.data
        )
        db.session.add(new_film)
        db.session.commit()
        return render_template('index.html')
    return render_template('ajouter_film.html', form=form)

@main.route('/films/<int:id>/critique', methods=['GET', 'POST'])
def film_critique(id):
    form = CritiqueForm()
    film = Film.query.get_or_404(id)
    if form.validate_on_submit():
        new_critique = Critique(
            contenu=form.contenu.data,
            film=film,
        )
        db.session.add(new_critique)
        db.session.commit()
        return render_template('film_detail.html', film=film)
    return render_template('ajouter_critique.html', form=form, film=film)


@main.route('/join-auteur', methods=['GET', 'POST'])
def insert_auteur():
        new_auteur = Auteur(
            nom="Trevor P Willson",
            date_de_naissance="1965-03-15",
            country="USA"
        )
        db.session.add(new_auteur)
        db.session.commit()
        return render_template('index.html')
@main.route('/join-book/<int:id>', methods=['GET', 'POST'])
def insert_book(id):
        auteur = Auteur.query.get_or_404(id)
        new_book = Livre(
            titre="Bryant Inside",
            date_de_publication="1993-05-16",
            genre="Horror",
            auteur_id = auteur
        )
        db.session.add(new_book)
        db.session.commit()
        return render_template('index.html')
@main.route('/join-user', methods=['GET', 'POST'])
def insert_user():
        user = [
            Utilisateur(nom="Quentin", email="Quentin@email.com"),
            Utilisateur(nom="Brandon", email="Brandon@email.com"),
            Utilisateur(nom="Grominet", email="Grominet@email.com")
            ]
        db.session.add_all(user)
        db.session.commit()
        return render_template('index.html')

@main.route('/join-user', methods=['GET', 'POST'])
def insert_user():
        user = [
            Utilisateur(nom="Quentin", email="Quentin@email.com"),
            Utilisateur(nom="Brandon", email="Brandon@email.com"),
            Utilisateur(nom="Grominet", email="Grominet@email.com")
            ]
        db.session.add_all(user)
        db.session.commit()
        return render_template('index.html')