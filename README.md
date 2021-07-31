# Examen-1Bimestre
Examen de primer bimestre 30/07/2021

Ejercicio 1:

#Librerias importadas
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
#APIS
ckey = "38wwOoHHCJy0cjgMBqjPzDGLF"
csecret = "fjogk0ofjk1VBrG2xZcC1bxce2tVR6DkFbQPjUeh5wn9HB1APV"
atoken = "115946548-kX87o1QHjrHmsnycH33Yc2KMb8yPuW3r6IibIROm"
asecret = "SNPXYgjyAhkafXT8Uslws4MAP0rlLKcpa2zvHiq1Ovr36"

#Crear el couchDB
couch=couchdb.Server('http://chriss:Beidou100%@127.0.0.1:5984')
try:
    print("Base de datos creada")
    db= couch.create('1')
except:
    print("Se entro a la base de datos")
    db=couch['1']

#Se usa la librearia de tweepy.streaming para poder realizar un track de los post de twitter
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
#TRACK POSTS DE TWITTER EN ESTAS LOCALIZACIONES
twitterStream.filter(locations=[-78.517469,-0.241575,-78.499754,-0.222349])
twitterStream.filter(locations=[11.4037,41.7901,13.9414,43.568])    
twitterStream.filter(locations=[-79.918329,-2.234556,-79.85351,-2.171157])  

Ejercicio 2:
#Librerias importadas
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#API
ckey = "38wwOoHHCJy0cjgMBqjPzDGLF"
csecret = "fjogk0ofjk1VBrG2xZcC1bxce2tVR6DkFbQPjUeh5wn9HB1APV"
atoken = "115946548-kX87o1QHjrHmsnycH33Yc2KMb8yPuW3r6IibIROm"
asecret = "SNPXYgjyAhkafXT8Uslws4MAP0rlLKcpa2zvHiq1Ovr36"
#ENLACE CON COUCHDB
couch=couchdb.Server('http://chriss:Beidou100%@127.0.0.1:5984')
try:
    print("Base de datos creada")
    db= couch.create('2')
except:
    print("Se entro a la base de datos")
    db=couch['2']
    
#SACA INFORMACION DE TWITTER
class listener(StreamListener):
    #DEFINE LOS CAMPOS Y LOS TRANSFORMA EN JHONSON
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

#SE REALIZA UN TRACK DE LOS POST EN TWITTER QUE SE HAN REALIZADO CON UNA CATEGORIA
twitterStream.filter(track=['Juegos Olimpicos'])
