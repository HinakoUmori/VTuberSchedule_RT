import authenticate

def tweet(prmCK, prmCS,prmAT, prmAS, prmMessageList) :
    try :
        token = authenticate.Auth(prmCK, prmCS,prmAT, prmAS)

        for i in prmMessageList :
            url = "https://api.twitter.com/1.1/statuses/update.json"
            params = {'status': i}
            token.post(url, params = params)

    except Exception as e :
        print(e)

# messageList = ['(テスト)', '(テスト2)']
# CK = ''
# CS = ''
# AT = ''
# AS = ''
#
# tweet(CK, CS, AT, AS, messageList)
