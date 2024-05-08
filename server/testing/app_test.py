from app import app

import json

from models import db, Subordinate, Manager

class TestApp:
    '''This is a Flask Application in flask_app.py'''

    def test_has_a_subordinates_route(self):
        '''has an endpoint "/subordinates"'''
        response = app.test_client().get('/subordinates')
        assert (response.status_code == 200)

    def test_has_subordinate_by_id(self):
        '''has a resource available at "/subordinates/<int:id>"'''
        response = app.test_client().get('/subordinates/1')
        assert (response.status_code == 200)

    def test_subordinate_by_id_route_returns_one_subordinate(self):
        '''returns a JSON object representing one Subordinate object at "/subordinates/<int:id>"'''
        response = app.test_client().get("/subordinates/1")

        data = json.loads(response.data.decode())

        assert (isinstance(data, dict))
        assert(data["id"])
        assert(data["name"])

    def test_subordinate_by_id_patch_route_updates_subordinate_name(self):
        '''returns JSON representing the updated Subordinate object with name="Mysterious Subordinate" at "/subordinates/1"'''
        with app.app_context():
            subordinate_1 = Subordinate.query.filter_by(id=1).first()
            subordinate_1.name = "Joel Nyongesa"

            db.session.add(subordinate_1)
            db.session.commit()

            response = app.test_client().patch(
                '/subordinates/1',
                json = {
                    "name": "Mysterious Subordinate"
                }
            )

            data = json.loads(response.data.decode())

            assert(isinstance(data, dict))
            assert(data["id"])
            assert(data["name"] == "Mysterious Subordinate")

    def test_creates_subordinate(self):
        '''can create a new subordinate through "/subordinates" route'''

        with app.app_context():
            new_subordinate = Subordinate.query.filter_by(name="Second Mysterious Subordinate").first()

            if new_subordinate:
                db.session.delete(new_subordinate)
                db.session.commit()

            response = app.test_client().post(
                '/subordinates',
                json = {
                    "name": "Second Mysterious Subordinate",
                }
            )

            subordinate = Subordinate.query.filter_by(name="Second Mysterious Subordinate").first()

            assert (response.status_code == 201)
            assert (response.content_type == "application/json")
            assert subordinate.id

    def test_has_a_managers_route(self):
        '''has an endpoint "/managers"'''
        response = app.test_client().get('/managers')
        assert (response.status_code == 200)