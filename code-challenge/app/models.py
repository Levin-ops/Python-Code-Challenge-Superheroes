from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

# This Hero class has a one-to-many relationship 
# with the HeroPower class through the powers attribute.
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    powers = db.relationship('Power', secondary='hero_power', back_populates= 'heroes')


class Power(db.Model):
    __tablename__ = 'powers'

# This Power class has a one-to-many relationship with the
# HeroPower class through the heroes attribute.

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    heroes = db.relationship('Hero', secondary='hero_power', back_populates= 'powers')



class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

# This HeroPower class is a join table that connects Hero
# and Power classes with a many-to-many kind of relationship.

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'))
    hero = db.relationship('Hero', back_populates='powers')
    power = db.relationship('Power', back_populates='heroes')
# add any models you may need. 