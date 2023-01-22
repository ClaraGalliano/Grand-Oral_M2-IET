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

with open('hpalme.txt', 'w') as ficRes:
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
                                    ficRes.write(EnTeteIram)
                                    try:
                                        ficRes.write(unicode(donne[u'comment']))
                                    except:
                                        print (type(donne[u'comment']))
                                        ficRes.write(donne[u'comment'].encode('utf8'))
                                    ficRes.write('\n')
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
            #{u'city': None, u'first_name': u'nathalie', u'last_name': u'gobin', u'display_name': u'nathalie GOBIN', 
            #u'description': None, u'locale': u'fr', 
            #u'photo': {u'url': u'photos/4/sl/qx/aCSlqxxCuEnxfHG-fullsize.jpg', u'id': 43243656, 
            #u'sizes': {u'small': {u'url': u'//d22r54gnmuhwmk.cloudfront.net/photos/4/sl/qx/aCSlqxxCuEnxfHG-48x48-noPad.jpg?1425023440', u'processing': False, u'size': {u'width': 48, u'height': 48}}, 
            #           u'large': {u'url': u'//d22r54gnmuhwmk.cloudfront.net/photos/4/sl/qx/aCSlqxxCuEnxfHG-400x400-noPad.jpg?1425023441', u'processing': False, u'size': {u'width': 400, u'height': 400}}, 
            #           u'medium': {u'url': u'//d22r54gnmuhwmk.cloudfront.net/photos/4/sl/qx/aCSlqxxCuEnxfHG-128x128-noPad.jpg?1425023440', u'processing': False, u'size': {u'width': 128, u'height': 128}}, 
            #           u'xlarge': {u'url': u'//d22r54gnmuhwmk.cloudfront.net/photos/4/sl/qx/aCSlqxxCuEnxfHG-800x800-noPad.jpg?1455899937', u'processing': False, u'size': {u'width': 800, u'height': 800}}}}, 
            #u'id': 163734699, u'short_display_name': u'nathalie', u'country_code': u'FR', u'state_code': None, u'slug': u'163734699'}    
            #champs = [u'comment', u'user_id', u'created_at', u'petition_id', u'likes', u'id', u'petition', u'user']
            
    

                
                    
        #EnTeteIram = "**** *nom_"+Nom *date_["created_at"] *ville_['city'](avec quand même la variable en cas d'info non renseignée, et "none" en donnée) *pays_['country'] *likes_['likes']  *userid_['userid'] *commentid_['id']    
        #ficRes.write()
#        for champ in champs:
#    for champ in champs:
#        ficRes.write(champ+';')
#    ficRes.write('\n')    
#    for donne in comments:
#        for champ in champs:
#            ficRes.write(str(donne[champ])+';')
#        ficRes.write('\n')   
        
    
