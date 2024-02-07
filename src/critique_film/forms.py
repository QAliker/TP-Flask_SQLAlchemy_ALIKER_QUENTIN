from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, IntegerField


class InscriptionForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Inscription')


class AjoutFilmForm(FlaskForm):
    titre = StringField('Titre', validators=[DataRequired()])
    realisateur = StringField('Réalisateur')
    annee_sortie = IntegerField('Année de Sortie')
    genre = StringField('Genre')
    submit = SubmitField('Ajouter le Film')


