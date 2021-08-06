import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#APIS de TWiTTER


import couchdb
import random as rd


# Enlace de COCHDB

try:
    print("Base de datos creada")
    db= couch.create('1')
except:
    print("Se entro a la base de datos")
    db=couch['1']

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

twitterStream.filter(locations=[-78.517469,-0.241575,-78.499754,-0.222349])
twitterStream.filter(locations=[11.4037,41.7901,13.9414,43.568])    
twitterStream.filter(locations=[-79.918329,-2.234556,-79.85351,-2.171157])  
