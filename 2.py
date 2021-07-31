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

twitterStream.filter(track=['Juegos Olimpicos'])