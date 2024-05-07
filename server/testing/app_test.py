from app import app

import json

from models import db, Subordinate, Manager

class TestApp:
    '''This is a Flask Application in flask_app.py'''

    def test_has_a_subordinates_route(self):
        '''has an endpoint "/subordinates'''
        response = app.test_client().get('/subordinates')
        assert (response.status_code == 200)