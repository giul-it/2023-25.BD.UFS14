
from MyProjFolder.mongo_database import sperofunzioni, transform_cursor_to_list
from jsonschema import validate

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

#unit test
collection = [
    {"_id": 1, "nome": "Mario", "età": 30, "città": "Roma"},
    {"_id": 2, "nome": "Luigi", "età": 25, "città": "Milano"},
    {"_id": 3, "nome": "Peach", "età": 28, "città": "Napoli"},
    {"_id": 4, "nome": "Toad", "età": 22, "città": "Torino"},
    {"_id": 5, "nome": "Daisy", "età": 27, "città": "Bologna"},
    {"_id": 6, "nome": "Wario", "età": 35, "città": "Firenze"},
    {"_id": 7, "nome": "Yoshi", "età": 20, "città": "Palermo"},
    {"_id": 8, "nome": "Birdo", "età": 32, "città": "Genova"},
    {"_id": 9, "nome": "Koopa", "età": 31, "città": "Venezia"},
    {"_id": 10, "nome": "Kamek", "età": 29, "città": "Catania"},
    {"_id": 11, "nome": "Nabbit", "età": 24, "città": "Verona"},
    {"_id": 12, "nome": "Lemmy", "età": 26, "città": "Bari"},
    {"_id": 13, "nome": "Iggy", "età": 23, "città": "Trieste"},
    {"_id": 14, "nome": "Ludwig", "età": 36, "città": "Reggio Calabria"},
    {"_id": 15, "nome": "Roy", "età": 33, "città": "Messina"},
    {"_id": 16, "nome": "Morton", "età": 34, "città": "Modena"},
    {"_id": 17, "nome": "Wendy", "età": 29, "città": "Ravenna"},
    {"_id": 18, "nome": "Pinky", "età": 21, "città": "L'Aquila"},
    {"_id": 19, "nome": "Puff", "età": 28, "città": "Sassari"},
    {"_id": 20, "nome": "Shy Guy", "età": 22, "città": "Catanzaro"}
]
print(type(collection))

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

