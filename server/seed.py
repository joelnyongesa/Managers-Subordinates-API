from faker import Faker
from models import db, Subordinate, Manager
from app import app
from random import choice as rc

fake = Faker()

with app.app_context():

    print("Emptying the database...")

    Subordinate.query.delete()
    Manager.query.delete()

    print("Database Emptied!")

    managers = []
    departments = ["engineering", "sales", "growth & partnerships", "customer relations"]

    for _ in range(15):
        manager = Manager(
            name = fake.name(),
            department = rc(departments)
        )

        managers.append(manager)

    print("Adding Managers...")
    db.session.add_all(managers)

    subordinates = []

    for _ in range(20):
        subordinate = Subordinate(
            name = fake.name(),
            manager = rc(managers)
        )

        subordinates.append(subordinate)

    print("Adding Subordinates...")

    db.session.add_all(subordinates)

    db.session.commit()

    print("Done Seeding! Happy coding!")