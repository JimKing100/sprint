# Import Flask package

from decouple import config
from flask import Flask, render_template
from TEST.models import DB, User
import swapi
import requests


def create_app():
    # Create Flask web server, makes the application
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    # Routes determine location
    @app.route("/")
    def home():
        DB.drop_all()
        DB.create_all()

        response = requests.get("https://swapi.co/api/people/?search=l")
        data = response.json()
        person = data['results'][0]
        # person = swapi.get_person(1)
        person1 = person['name']
        person = data['results'][1]
        # person = swapi.get_person(2)
        person2 = person['name']
        db_user = User(id='1', name=person1)
        DB.session.add(db_user)
        db_user = User(id='2', name=person2)
        DB.session.add(db_user)
        DB.session.commit()
        people = User.query.filter(User.name == person2)
        return render_template('home.html', title=person1, people=people)
    return app
