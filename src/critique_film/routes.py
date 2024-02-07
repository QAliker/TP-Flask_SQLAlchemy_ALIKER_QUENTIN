from flask import Blueprint, render_template
from .forms import InscriptionForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/inscription', methods=['GET', 'POST'])
def inscription():
    # opérations pour enregistrer le formulaire
    form = InscriptionForm()
    return render_template('inscription.html', form=form)
