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
    
    def post(self):

        new_subordinate = Subordinate(
            name = request.get_json()["name"],
        )

        db.session.add(new_subordinate)
        db.session.commit()

        new_subordinate_dict = new_subordinate.to_dict()

        response = make_response(jsonify(new_subordinate_dict), 201)

        return response    
    
class SubordinateByID(Resource):
    def get(self, id):
        subordinate = Subordinate.query.filter_by(id=id).first().to_dict()

        response = make_response(jsonify(subordinate), 200)
        
        return response
    
    def patch(self, id):
        subordinate = Subordinate.query.filter_by(id=id).first()

        for attr in  request.get_json():
            setattr(subordinate, attr, request.get_json()[attr])

        db.session.add(subordinate)
        db.session.commit()

        subordinate_dict = subordinate.to_dict()

        response = make_response(jsonify(subordinate_dict), 200)

        return response


    
class Managers(Resource):
    def get(self):
        managers = [manager.to_dict() for manager in Manager.query.all()]

        response = make_response(jsonify(managers, 200))

        return response
    

api.add_resource(Subordinates, '/subordinates', endpoint="subordinates")
api.add_resource(SubordinateByID, "/subordinates/<int:id>", endpoint='subordinate_id')
api.add_resource(Managers, '/managers', endpoint="managers")

if __name__ == "__main__":
    app.run(port=8080, debug=True)