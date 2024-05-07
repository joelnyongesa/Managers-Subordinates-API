from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Subordinate, Manager

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app=app, db=db)

db.init_app(app=app)

api = Api(app=app)

class Subordinates(Resource):
    def get(self):
        subordinates =[subordinate.to_dict() for subordinate in Subordinate.query.all()]

        response = make_response(jsonify(subordinates), 200)
        return response
    

api.add_resource(Subordinates, '/subordinates', endpoint="subordinates")

if __name__ == "__main__":
    app.run(port=8080, debug=True)