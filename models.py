from google.appengine.ext import ndb

class OfferModel(ndb.Model):
    lenderAddress = ndb.StringProperty(required=True) # loan creator wallet adddress
    market = ndb.StringProperty(required=True) # token pair
    wranglerAddress = ndb.StringProperty(required=True) # wrangler address
    loanTokenAddress = ndb.StringProperty(required=True) # OMG contract address
    loanTokenSymbol = ndb.StringProperty(required=True) # OMG contract address
    loanTokenAmount = ndb.StringProperty(required=True) # 1000
    loanCostTokenSymbol = ndb.StringProperty(required=True) # 1000
    loanCostTokenAddress = ndb.StringProperty(required=True) # ETH contract address
    loanCostTokenAmount = ndb.StringProperty(required=True) # 100
    loanInterestTokenSymbol = ndb.StringProperty(required=True) # 0.01
    loanInterestTokenAmount = ndb.StringProperty(required=True) # 0.01
    loanInterestTokenAddress = ndb.StringProperty(required=True) # ETH contract address
    ecSignature = ndb.StringProperty(required=True)

class OrderModel(ndb.Model):
    exchangeContractAddress = ndb.StringProperty(required=True)
    maker = ndb.StringProperty(required=True)
    taker = ndb.StringProperty(required=True)
    makerTokenAddress = ndb.StringProperty(required=True)
    takerTokenAddress = ndb.StringProperty(required=True)
    feeRecipient = ndb.StringProperty(required=True)
    makerTokenAmount = ndb.StringProperty(required=True)
    takerTokenAmount = ndb.StringProperty(required=True)
    makerFee = ndb.StringProperty(required=True)
    takerFee = ndb.StringProperty(required=True)
    expirationUnixTimestampSec = ndb.StringProperty(required=True)
    salt = ndb.StringProperty(required=True)
    ecSignature = ndb.JsonProperty(required=True)
