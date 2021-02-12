import authenticate

def retweet(prmCK, prmCS,prmAT, prmAS, prmIDList) :
    try :
        token = authenticate.Auth(prmCK, prmCS,prmAT, prmAS)

        for i in prmIDList :
            url = "https://api.twitter.com/1.1/statuses/retweet/{}.json".format(i)
            params = {'id': i}
            token.post(url, params = params)

    except Exception as e :
        print(e)

# idList = [13551055988455424045]
# CK = ''
# CS = ''
# AT = ''
# AS = ''
#
# retweet(CK, CS, AT, AS, idList)
