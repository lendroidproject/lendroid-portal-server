from flask import Flask, render_template, request, jsonify, abort
from flask_restful import Resource, Api
from google.appengine.api import app_identity
from google.appengine.ext import ndb

app = Flask(__name__)
app.config['DEBUG'] = False
api = Api(app)


class OfferModel(ndb.Model):
    creatorAddress = ndb.StringProperty()

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

class Index(Resource):
    def get(self):
        """ Render the Index page"""
        return render_template('index.html')

class Offers(Resource):
    def get(self):
        """ Return a list of existing loan offers"""
        offers = OfferModel.query().fetch()
        offers_list = [{'id': offer.creatorAddress } for offer in offers]
        return jsonify(offers=offers_list)

    def post(self):
        if not request.json:
            abort(400, {"error": "Expected application/json"})
        offer = OfferModel(creatorAddress="0x123456")
        key = offer.put()
        return { 'id': key.id() }, 201

api.add_resource(Offers, '/offers', endpoint='offers')
api.add_resource(Index, '/', endpoint='index')
