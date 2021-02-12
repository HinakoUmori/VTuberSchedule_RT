import sys
sys.path.append('../')
from tweet import tweet
from retweet import retweet
from getUserTL import get_UserTL
from enum import Enum, auto
import time
import datetime
import re

class KeyList(Enum):
    TEXT = 0
    ID = auto()

CK = ''
CS = ''
AT = ''
AS = ''

while True :
    try :
        TL_list = []
        RT_list = []
        key = ['text', 'id']
        TL_list.append(get_UserTL(CK, CS, AT, AS, 'AniMare_cafe', 20, None, None, True, key))
        TL_list.append(get_UserTL(CK, CS, AT, AS, 'HNST_official', 20, None, None, True, key))
        TL_list.append(get_UserTL(CK, CS, AT, AS, 'SugarLyric_PI', 20, None, None, True, key))
        TL_list.append(get_UserTL(CK, CS, AT, AS, 'Vtuber_ApArt', 20, None, None, True, key))

        word_list = ['スケジュール', 'お休み', '日時', '予定']

        for i in TL_list :
            for k in i :
                for j in word_list :
                    if j in k[KeyList.TEXT.value] :
                        # RT_list.append(k[KeyList.ID.value])
                        RT_list.append(k[KeyList.ID.value])
                    elif re.findall('\d+:\d+', k[KeyList.TEXT.value]) != [] :
                        RT_list.append(k[KeyList.ID.value])

        retweet(CK, CS, AT, AS, RT_list)
        now = datetime.datetime.now()
        print(now)
        f = open('timeLog.txt', 'a', encoding = 'UTF-8')
        f.write('{}\n'.format(str(now)))
        f.close()

    except Exception as e :
        f = open('timeLog.txt', 'a', encoding = 'UTF-8')
        f.write('{}\n'.format(e))
        f.close()
        print(e)
    finally :
        time.sleep(300)
