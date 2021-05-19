# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:16:46 2021

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:28:02 2021

@author: user
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from xml.etree import ElementTree
import pandas as pd




# decode_key = unquote('EJt698FcsEYZrXpbxwnR6lN%2BpmOv5TXURNhFnUXVnq%2FIyvfhaJrgwqVyAG1Ap90PeSVYoe%2FDR77phWtubWLBfA%3D%3D')
servicekey = '1lsk6Np8Eof/L+6STErYet4sFcoGPtD2koMJvc5TdYEUDwvR7OiF3IX7wsZrwIKlh5s0ofxv9In4frqUYtLIgg=='
url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : servicekey, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '9999', quote_plus('zcode') : '11' })
print(url+queryParams)


request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()


root = ElementTree.fromstring(response_body)

df = pd.DataFrame()
for item in root.iter('item'):
    item_dict = {}
    item_dict = {}
    item_dict['statNm'] = item.find('statNm').text
    item_dict['addr'] = item.find('addr').text
    item_dict['busiNm'] = item.find('busiNm').text
    item_dict['stat'] = item.find('stat').text
    item_dict['powerType'] = item.find('powerType').text
    
    df = df.append(item_dict, ignore_index = True)
print(df)    

df.to_csv(path_or_buf=r"ev_seoul2.csv", encoding='euc-kr')
    
print(df)

