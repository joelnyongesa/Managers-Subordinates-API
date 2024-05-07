from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# We are creating two classes: Manager and Subordinate
# Relationship: One manager, many subordinates, One subordinate, one manager

class Subordinate(db.Model, SerializerMixin):

    __tablename__ = "subordinates"

    serialize_rules = ("-manager.subordinates",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey("managers.id"))

    def __repr__(self):
        return f"Subordinate: {self.name}"


class Manager(db.Model, SerializerMixin):

    __tablename__ = "managers"

    serialize_rules = ("subordinates.manager")

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    department = db.Column(db.String, nullable=False)

    subordinates = db.relationship("Subordinate", backref="manager")

    def __repr__(self):
        return f"Manager: {self.name}"