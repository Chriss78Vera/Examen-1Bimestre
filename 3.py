
from typing import Text
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
#CONECION CON MONGO
#CONECT = MongoClient('mongodb+srv://Chriss:Beidou100@cluster0.3hs4q.mongodb.net/test?authSource=admin&replicaSet=atlas-13ecwb-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
#CREAMOS LA BASE
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring)) 

data= requests.get("https://www.eluniverso.com/deportes/otros-deportes/juegos-olimpicos-de-tokio-2020-calendario-y-horario-de-los-deportistas-ecuatorianos-nota/")
soup=BeautifulSoup(data.content)
titulos=soup.find_all("h1")
subtitulos=soup.find_all("h2" )
texto=soup.find_all("h3")

titulos_1=[]
recorrido=[]
subtitulos_1=[]
texto_1=[]


for element in titulos:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    titulos_1.append(limpio.strip())

for element in subtitulos:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    subtitulos_1.append(limpio.strip())


print(titulos_1)


print(subtitulos_1)


print(texto)
