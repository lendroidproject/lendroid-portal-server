from google.appengine.ext import ndb

class OfferModel(ndb.Model):
    lenderAddress = ndb.StringProperty(required=True) # loan creator wallet adddress
    loanTokenAddress = ndb.StringProperty(required=True) # OMG contract address
    loanTokenAmount = ndb.StringProperty(required=True) # 1000
    loanCostTokenAddress = ndb.StringProperty(required=True) # ETH contract address
    loanCostTokenAmount = ndb.StringProperty(required=True) # 100
    loanInterestTokenAmount = ndb.StringProperty(required=True) # 0.01
    loanInterestTokenAddress = ndb.StringProperty(required=True) # ETH contract address
    ecSignature = ndb.StringProperty(required=True)
