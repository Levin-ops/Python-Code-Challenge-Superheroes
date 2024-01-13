from random import choice as rc
from faker import Faker
from app import create_app
from models import db, Hero, Power, HeroPower

fake = Faker()

hero_names = [fake.first_name() for _ in range(4)]

def make_seed_data():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Seed data
    heroes = []
    powers = []
    hero_powers = []

    for i in range(4):
        hero = Hero(
            name=rc(hero_names),
            super_name=fake.first_name(),
        )
        heroes.append(hero)
        db.session.add(hero)

        power = Power(
            name=fake.word(),
            description=fake.sentence(),
        )
        powers.append(power)
        db.session.add(power)

        hero_power = HeroPower(
            hero=hero,
            power=power,
        )
        hero_powers.append(hero_power)
        db.session.add(hero_power)

    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    
    with app.app_context():
        make_seed_data()