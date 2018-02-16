from flask import Flask, render_template, request, jsonify, abort
from flask_restful import Resource, Api
from google.appengine.api import app_identity
from flask_cors import CORS

import models

app = Flask(__name__)
app.config['DEBUG'] = True

# Add support for Restful api
api = Api(app)

# Add CORS support for all domains
CORS(app, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)

# Market Information
MARKET_INFO = {
  'tokens': {
    '0x73de023fc01ab': {
      'symbol': 'OMG',
      'name': 'Omisego',
      'decimals': 18,
      'logo_url': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAIfUExURRpT7wlG7x9X8BxU8BtU8BxV8B5W8BpT8P///x1V8ApH7w5K7xZQ8BtT8BVP8A1J7xdR8CBY8BlS8AxI7xFM7wtI7w9L7wlH7562+RhR8B1W8BBL7xRP8BhS8Jiy+P3+/xRO8BNO8BdQ8CNa8RJN7xBM7wJB7qa8+f7+/ypf8Stg8Q1K7yRa8S1h8dDc/BlT8Iel95ix+Pv8/whF7wdF79zl/cHR+wZE7xJN8NXf/GOK9ZCs+CJZ8R9W8CZc8crX/JOu+Pb4/kt481eB9Pn7/+vw/sjW++zx/q/D+gA97idd8Sle8WWM9QxJ72mO9drj/czY/GCH9RNN8D9v8uLq/TJl8o2q9xVQ8O7y/uHp/WGJ9SVb8Ud18y9j8Y6q+LfJ+vj6/wtH73+f9+Do/VaA9Iqn94+r+Pf5/r/P+7zN+7vM+zxs8jhp8muQ9d7m/She8dni/ZSu+MfV+8XU+/X4/vX3/u/z/q7C+jBk8TZo8py1+Nfh/CFY8M/b/MDQ+/z8/4Wj9/H1/jts8kFw8+Xs/eTr/XKV9q3B+tni/CJZ8MvY/IOi926S9WCI9c3Z/KC4+Shd8fT3/pmy+Iyo9w9K72yR9erv/uLp/WSK9dbg/NXg/GGI9dHc/CRb8VmC9JKt+LjK+vf5/3WX9qe9+fD0/uPq/QA/7srX+5u0+Iim901580x48+3y/gFA7u3x/gA+7unu/qS7+WiO9Sxh8aK5+b2+8wQAAAABdFJOU/4a4wd9AAAB/0lEQVQ4y7XTVXfbQBAGUEva1c5IBsnsmNlhZmYsMzMzMzMzMzP3B1ZxEtepnD6139Oeo6vVamfGYGB/j+FfApLOyNKkBygoRi2K9jSPKX4U/gDCJK9a1HJ1IMoEq2RuEhwxHA+cDVOXBq/dfvlxsI5e2Fyx+8wGGbOA4A3ATPeVO/D1HS+2wvnyPjiyckSkAdomQ8DOcZFk14cvfXCXkyqLzx7Ln0PGAKmrnuL08LzZ2N0zAG8/8aLqOgFHOXEUEHM+NHI8Yzz3rXco9T6u7U1DJ9cuwwwogNmuNPj5+Xuqwz4MwqcOO8YAM/nm1dtYM++JvXrzA9oSqnjQdhxWZT7B8hyn4YbNxd0MwNDrp9BZK1VFD61Z5MsckpFYEu41PqmG63ZPSz2sL3O3w/zC37/JiDX8/P6z9oe37AxD59q6oWLdQkv2RZWip3+w4cGjfkatVJFIQVSOj7tqwdz0ArS40Ui0YlnNEUqzi0X8eBncnY+TUKMwrdKm0apngCithksJp5y4CMslUd8wJmvp3JpaHlGUSlaETXpAfMVQNvymKJWniiJED4wLgvurVMbUyj270K8HjMrbe5tlRNuWnUscmKNp0dkBO/Z64/tKgjPsNFdXY+EmgANboWuajLnbnlo2bmvtWTzLghPNBU7nLBZXCCceHEGkVBT+82zmzi9fyGIIDF11YQAAAABJRU5ErkJggg=='
    },
    '0x023e1abfc073d': {
      'symbol': 'ETH',
      'name': 'Ethereum',
      'decimals': 18,
      'logo_url': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAKdUExURUxpcX9/fy4vL////wAAAKqqqj8/PwAAAFVVVX9/fzU2Ni0uLjQ1NS8wMC8wMDAxMYGCg4aHiC8wMBISEnx9foKDhP///zEyMi4uLi8vLy8wMC4wMCwzMzAxMS4wMC8vLzAwMAAAAE1NU4KDhH+CgoGCg4GCg4uLi2RkZIGBg4SFhisrK4WGhy4yMi0wMICBgi8vLzo7Ozg4OC4uLi4vL4CCg4KCgr+/vy8wMDAxMYaHiHd3eCoqKjIyMoCBgjAxMYKCgoSFhgBVVTMzMy8vLzQ1NVVVVYCBgo2NjXJzdIWGhzMzM4SEhRcXF3+BgSsrKwAAAD0+PoaGiYKEhnt8fS0uLmNjYzAxMX9/f3x9fiYmJhYXF6qqqn19fXiHhy8wMC8vLw0NDTQ1NWhpaS0vLy8vLy0tLS8wMC8wMImKi3R0dhQUFDE1NRMTExMTEy4vL0JCQhEREXt8fRQUFC8yMhMTEzExMTEyMhMTEzExMRMTE4iJioODhFVVqj9AQBMUFBISEhUVFYCBg4CAgzU1NS8wMAcHB4ODgzU2NiYmJoCAgzM0NDIzMzQ1NX9/fzc4ODAwMJGRkYCBgjExMYGBhYiIijY4OIKChICAgoWGhyoqKoOEhYSFhn19foeIiSsrK4SFhYSFhpKSkhgYGDc5OTY2NoKDhP///4aGiTU3N4SEhh4eHoKDhDU2NjIzMxMTEzEyMjQ1NS8wMBISEhUVFTAxMS4vL4aHiHx9foOEhTc4OBQUFIqLjIGCg4KDhDM0NImKixEREYWGhzY3N42Oj4iJio+QkTg5OSorKxQTExwdHTAyMi0uLiAhISgpKVBRUXZ3eHt8fU1OToyNjm9wcUdISBoaGicoKImLixIREWxtbRcXF35/gISFhoeIiZeCJKAAAACtdFJOUwAE/AECAwQBAwL+/Pz8/v78/v38/vwC/AtQ3oQo97S4JQQr3VD+/QsrhPyG90Jf/BDWCVOmtCcE4fb81pfft/wl9gMjgfsk/gnA/Arbi4BMA8BMh/zcJPJC+/35CVMRwjsn/f17XBz7+t+XvDT+/OCLV/3f4P2R/vtchv7hA/n4svynXzDBISP9KFv76P4cvJcz4Fc7kN/Be+AG/PLn/lLB+i9Ssvj9BluGliH79CoX3QAAAelJREFUOMtjYCAJcLKHubGz4FHAweAZCCRwAlaGoJ2H/XGrYOf08HHnCvVmYcehgJHB70gIzwYXBjZcLnRw9BLhYrJUwOFOVgbTPaI71nKvk8PuClYGlQMCO3es3ca7ThKbCnZOdWVBNZACIX4pCSzuZGXQvCywb9/Ftds2Ma2TxjSCk91MR0t17/a9uzZt4uOVlcFwJyuD3QH97dsvnD97YsNppg3y6EawMsTesDp05dLaMyfXnzq31X6dMaoKZvaYTMHkqxs2rd2/ZfPBzdei+G2N2NlRIinrVt3WrWvXrl23ZfP69TcPRl+3QTGCnbNAfCNPx8aNEAWleeuFfVF9ysnQ2b9rbXcvSEFuxe7d2YkMASjytV0TGSZPO76RZ90W4fW7iwsZclKdWFAc2TdpqhjDyqXHxRvX11cxiJXlp6E4EuigKcdmrmBYvWTt7YY2hsqSjQnoAcHIMOPY0QWLGOYvZmhp3bAxBSNNsLNyTp937+6q5bMmbN1QHs/CgRFbnAztcxYuOzK3Z51QRrgzAwu2BNe8Z83sO7u409fpYU90jAxNe0RFuLj3m+BIlMyccTXVRUl8Fga4kjUrQ8TRSNdNurgzBiND8KHD2rhSPcivHObWhooc7HgyL4OGEgO+zMvADkbIAAARJJqN9Q/B/QAAAABJRU5ErkJggg=='
    },
    '0x048e1a2d7803a': {
      'symbol': 'ZRX',
      'name': '0x Protocol Token',
      'decimals': 18,
      'logo_url': 'data:image/png;base64,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'
    },
  },
  'markets': [
    {
      'pair': 'OMG/ETH',
      'baseTokenAddress': '0x73de023fc01ab',
      'quoteTokenAddress': '0x023e1abfc073d'
    },
    {
      'pair': 'ZRX/ETH',
      'baseTokenAddress': '0x048e1a2d7803a',
      'quoteTokenAddress': '0x023e1abfc073d'
    }
  ]
}

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

@app.route('/create-offers', methods=['GET'])
def createOffers():
      return render_template('index.html')

@app.route('/view-offers', methods=['GET'])
def viewOffers():
      return render_template('index.html')

@app.route('/commit-funds', methods=['GET'])
def commitOffers():
      return render_template('index.html')

@app.route('/deposit-funds', methods=['GET'])
def depositFunds():
      return render_template('index.html')

def output_html(data, code, headers=None):
    resp = app.make_response(data)
    resp.status_code = code
    return resp

class Index(Resource):
    def get(self):
        """ Render the Index page"""
        return output_html(render_template('index.html'), 200)

class Markets(Resource):
    def get(self):
        return jsonify(info=MARKET_INFO)

class Offers(Resource):
    def get(self):
        """ Return a list of existing loan offers"""
        offers = models.OfferModel.query().fetch()
        offers_list = [offer.to_dict() for offer in offers]
        return jsonify(offers=offers_list)

    def post(self):
      try:
        data = request.get_json(force=True)
        offer = models.OfferModel(**request.json)
        key = offer.put()
        return { 'id': key.id() }, 201
      except AttributeError as exc:
          abort(400, {"error": exc.message})
      except Exception as exc:
          abort(400, {"error": exc.message })


class Orders(Resource):
    def get(self):
        """ Return a list of existing loan offers"""
        orders = models.OrderModel.query().fetch()
        orders_list = [order.to_dict() for order in orders]
        return jsonify(orders=orders_list)

    def post(self):
        if not request.json:
            abort(400, {"error": "Expected application/json"})
        order = models.OrderModel(**request.json)
        key = order.put()
        return { 'id': key.id() }, 201

api.add_resource(Orders, '/orders', endpoint='orders')
api.add_resource(Offers, '/offers', endpoint='offers')
api.add_resource(Markets, '/markets', endpoint='markets')
api.add_resource(Index, '/', endpoint='index')
