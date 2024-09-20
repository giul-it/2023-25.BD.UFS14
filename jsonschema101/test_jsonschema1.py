#pytest cerca nella cartella file con il nome che inizia con test_ e dentro ai file cerca le funzioni
#che con il nome che inizia con test_
# content of test_sample.py
from jsonschema import validate

'''#primo test
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4'''

#secondo test
schema = {
    "type" : "object",
    "properties" : {
        "price" : {"type" : "number"},
        "name" : {"type" : "string"},
    },
}

def test_validation_success():
   assert validate_wrapper(instance={"name" : "Eggs", "price" : 34.99}, schema=schema) == True

def test_validation_fail():
    assert validate_wrapper(instance={"name" : "Eggs", "price" : "invalid"}, schema=schema,) == False
def validate_wrapper(instance, schema):
    try:
        validate(instance = instance, schema = schema)
        return True
    except:
        return False