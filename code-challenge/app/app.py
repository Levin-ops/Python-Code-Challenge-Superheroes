#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Hero, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ('''<h1> Phase 4 Code Challenge 1</h1>
                <h2>Superheroes</h2>''')

@app.route('/heroes')
def get_heroes():
    heroes = Hero.query.all()

    formated_output=[
        {"id":hero.id,
         "name":hero.name,
         "super_name":hero.super_name}
         for hero in heroes]
    
    response = make_response(
        jsonify(formated_output),
        200
    )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug = True)
