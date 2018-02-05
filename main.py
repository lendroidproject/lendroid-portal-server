import urllib
import json
from flask import Flask, render_template, request, jsonify, abort
from google.appengine.api import urlfetch, mail, app_identity
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['DEBUG'] = False
api = Api(app)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

class Index(Resource):
    def get(self):
        """ Render the Index page"""
        return render_template('index.html')
api.add_resource(Index, '/', endpoint='index')

class LoanOffer(Resource):
    def get(self):
        """ Return a list of existing loan offers"""
        return [{ 'id': 1, 'order': 'test order'}]

    def post(self):
        if not request.json:
            abort(400, {"error": "Expected application/json"})
        return { 'success': True }, 201
api.add_resource(LoanOffer, '/api/loan_offers', endpoint='loan_offers')
