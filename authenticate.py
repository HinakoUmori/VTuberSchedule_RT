from requests_oauthlib import OAuth1Session

def Auth(prmCK, prmCS,prmAT, prmAS) :
    token=OAuth1Session(prmCK, prmCS, prmAT, prmAS)
    return token
