# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 10:15:51 2018

@author: claro
"""
import pickle
import os
#import codecs
#import sys  
import unicodedata
import re
from textblob import TextBlob

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
alphnumspace = re.compile(r"[^a-zA-Z\d\s\_\*]")

#reload(sys)  
#sys.setdefaultencoding('utf8')
DejaVus = []

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
comments = []    
from datetime import datetime  
cpt = 0  
cptPac = 0
dejavu = 0

ficResPO = open ('po.txt', 'w')
ficResPS = open ('ps.txt', 'w')
ficResNO = open ('no.txt', 'w')
ficResNS = open ('ns.txt', 'w')

for fichier in os.listdir('.'):
    
    if fichier.endswith('hpalme.pkl'):
        print ("loading "), fichier
       # arg = raw_input('GO ???')
        with open(fichier, 'r') as fic:
        #    data=pickle.load(fic)
            while 1:
                try:
                    data = pickle.load(fic)['items']
                    cptPac +=1
                    try:
                        for donne in data:
                            cpt+=1
                            if donne['id'] not in DejaVus:
                                DejaVus.append(donne['id'])
                                #data2.append(donne)
                                Nom= donne['user'][u'first_name'].title()+ donne['user'][u'last_name'].title()#['firstname-accolé-à-lastname']
                                Date=datetime.strptime(donne['created_at'][:19], '%Y-%m-%dT%H:%M:%S').isoformat()
                                if Date is not None:
                                    pass
                                else:
                                    Date=u'2018'
                                if len(Nom)==0:
                                    Nom=u'Incognito'
                                Ville=donne[u'user'][u'city']
                                if Ville is None:
                                    Ville=u"Inconnue"
                                Pays=donne['user'][u'country_code']
                                if Pays is None:
                                    Pays = u"Inconnu"
                                Likes=unicode(donne['likes']) 
                                Uid = unicode(donne['user_id'])
                                CommentId =unicode(donne['id'] )
                                EnTeteIram = u"**** *Nom_"+Nom + u" *Date_"+Date + u" *Ville_"+Ville +u' *Pays_'+Pays + u' *Likes_'+Likes + u' *Uid_'+Uid + u' *CommentId_'+CommentId +u' \n'
                                EnTeteIram =  strip_accents(EnTeteIram)                                  
                                EnTeteIram = alphnumspace.sub('', EnTeteIram)
                              
                                blob=TextBlob(unicode(donne[u'comment']))
                                if blob.polarity > 0:
                                    if blob.subjectivity > 0.5:
                                      ficResPS.write(EnTeteIram)
                                      try:
                                          ficResPS.write(unicode(donne[u'comment']))
                                      except: 
                                          ficResPS.write(donne[u'comment'].encode('utf8'))
                                    else:
                                      ficResPO.write(EnTeteIram)
                                      try:
                                           ficResPO.write(unicode(donne[u'comment']))  
                                      except:
                                           ficResPO.write(donne[u'comment'].encode('utf8'))
                                else:
                                    if blob.subjectivity < 0.5:                                        
                                      ficResNO.write(EnTeteIram)
                                      try:
                                             ficResNO.write(unicode(donne[u'comment']))
                                      except:
                                              ficResNO.write(donne[u'comment'].encode('utf8'))
                                    else:
                                      ficResNS.write(EnTeteIram)
                                      try:
                                         ficResNS.write(unicode(donne[u'comment']))  
                                      except:    
                                          ficResNS.write(donne[u'comment'].encode('utf8'))                                       
                            else:
                                dejavu+=1
#                                    print donne
                            #print str(cpt) + " Commentaires. Traites :", len(DejaVus)
                    except:
                            print (" pas bon là...")
                except EOFError:
                        print (fichier, ' traité : ', len(DejaVus), " doublons ", dejavu)
                        print (cptPac, " paquets ", cpt, "commentaires")
                        break    
