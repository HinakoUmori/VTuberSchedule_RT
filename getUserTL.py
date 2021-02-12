import authenticate
import json

def get_UserTL(prmCK, prmCS,prmAT, prmAS, prmName, prmCount, prmSince, prmMax, prmTrim, prmKeyList) :

    try :
        token = authenticate.Auth(prmCK, prmCS,prmAT, prmAS)
        list_TL = []

        params ={
             'count'   : prmCount,        # 取得するtweet数
             'screen_name' : prmName,  # twitterアカウント名
             'trim_user' : prmTrim,
             'tweeet_mode' : 'extended',
             'since_id' : prmSince,
             'max_id' : prmMax
        }

        url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
        req = token.get(url, params = params)
        res = json.loads(req.text)
        for line in res:
            tmp_TL = []
            for key in prmKeyList :
                tmp_TL.append(line['{}'.format(key)])
                # tmp_TL.append(line)

            list_TL.append(tmp_TL)
        return list_TL

    except Exception as e :
        print(e)

# key = ['text']
# CK = ''
# CS = ''
# AT = ''
# AS = ''
# #
# print(get_UserTL(CK, CS, AT, AS, 'AniMare_cafe', 10, None, None, True, key))
