from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


#print(ingredienti)



def transform_cursor_to_list(collection):
    ingredienti = []
    for x in collection: 
        ingredienti.append(x)
    return ingredienti


def sperofunzioni(z):
    uri = "mongodb+srv://lucagiovagnoli:t7g^Fyi7zpN!Liw@ufs13.dsmvdrx.mongodb.net/?retryWrites=true&w=majority&appName=UFS13"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['INCI']
    d = db.Ingredienti.find({}, {"_id":0, "Nome_comune":1})
    #print(type(d))
    ingredienti = transform_cursor_to_list(d)
    y = ingredienti[z]
    bho = db.Ingredienti.find_one(y)
    return bho


print(type((sperofunzioni(11))))
print(sperofunzioni(11))

