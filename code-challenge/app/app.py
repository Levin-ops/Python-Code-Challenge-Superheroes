#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
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

    hero_dict=[
        {"id":hero.id,
         "name":hero.name,
         "super_name":hero.super_name}
         for hero in heroes]
    
    response = make_response(
        jsonify(hero_dict),
        200
    )

    return response

@app.route('/heroes/<int:hero_id>', methods = ['GET'])
def get_hero_by_id(hero_id):
    hero = Hero.query.get(hero_id)

    if request.method == 'GET':
        # if hero in None:
        #     response_body={
        #         "error":"Hero not found"
        #     }
        #     response = make_response(
        #         jsonify(response_body),
        #         404
        #     )
        #     return response
        
        powers_dict =[{
            "id":power.id,
            "name":power.name,
            "description": power.description
        } for power in hero.powers]


        hero_dict = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "powers": powers_dict
        }

        response = make_response(
            jsonify(hero_dict),
            200
        )

        return response




if __name__ == '__main__':
    app.run(port=5555, debug = True)
