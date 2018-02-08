from google.appengine.ext import ndb

class OfferModel(ndb.Model):
    lenderAddress = ndb.StringProperty(required=True)
    tokenPair = ndb.StringProperty(required=True)
    loanQuantity = ndb.IntegerProperty(required=True)
    loanToken = ndb.StringProperty(required=True)
    costAmount = ndb.IntegerProperty(required=True)
    costToken = ndb.StringProperty(required=True)
    ecSignature = ndb.StringProperty(required=True)
