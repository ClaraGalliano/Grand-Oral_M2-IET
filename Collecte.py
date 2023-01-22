# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:57:51 2018

@author: claro
"""

import requests
import time
import json
import pickle # bibliothèque de serialisation

Res = ''
Dern= False
cpt = 0
with open('nazanin.pkl', 'w') as fic:
    while not Dern or cpt>400000:
        url='https://www.change.org/api-proxy/-/petitions/lu-stop-à-l-utilisation-d-huile-de-palme/comments?limit=10&offset='+str(cpt)+"&order_by=voting_score"
        page = requests.get(url)
        if page.ok:
            data = json.loads(page.text)
            Dern = data['last_page']
            pickle.dump(data, fic)
            cpt +=10
#            print cpt
            time.sleep(3)
        else:
            Dern = True
#            print cpt
        
