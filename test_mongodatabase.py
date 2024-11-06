
from MyProjFolder.mongo_database import sperofunzioni, transform_cursor_to_list
from jsonschema import validate
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


schema = {
  "type": "object",
  "properties": {
    "_id": {
      "bsonType": "objectId"
      
    },
    "Nome_comune": {
      "type": "string"
    },
    "INCI_name": {
      "type": "string"
    },
    "main_link": {
      "type": "string"
    },
    "pdf_link": {
      "type": "string"
    },
    "pdf_date": {
      "type": "string"
    },
    "pdf_name": {
      "type": "string"
    },
    "pbc_data": {
      "type": "object",
      "properties": {
        "page": {
          "type": "string"
        },
        "valori": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "fonti": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": ["page", "valori", "fonti"]
    },
    "contesti_ld50": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "contesti_noael": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "valori_ld50": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "valori_noael": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}


#print(sperofunzioni(11))
lab = sperofunzioni(11)

#test assert
def test_diz():
    output = lab
    assert isinstance(output, dict) == True
    for chiave in output.keys():
        assert isinstance(chiave, str) == True
    assert isinstance(lab["_id"], str) == False

#test json schema
def validate_wrapper(instance, schema):
    try:
        validate(instance = instance, schema = schema)
        return True
    except:
        return False

def test_validation_success():
   assert validate_wrapper(instance=lab, schema=schema) == True

#test snapshot
def test_function_output_with_snapshot(snapshot):
    snapshot.snapshot_dir = 'snapshots'  # This line is optional.
    strjson = str(lab)
    snapshot.assert_match(strjson, 'un_ingrediente.txt')

