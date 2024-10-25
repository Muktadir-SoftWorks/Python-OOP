#data interchange format which is language independent
#understanding Json stracture
#Key Functions
# json.dumps() json.loads() json.dump() json.load()

#json object >>> Json string

import json

personOBJ = {

    "name":"Muktadir",
    "Age": 30,
    "title":["Engineer","Programmer"]
}
PersonJSON = json.dumps(personOBJ,indent=4)
print(PersonJSON)

#json string >>>> python object

# JSON String ----> Python Object

personJSON = '{"name": "John", "age": 30, "city": "New York"}'
personOBJ = json.loads(personJSON)
print(personOBJ['name'])


# Python Object ----> JSON String + File Write

personOBJ = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

with open("person.json", "w") as personJSONFile:
    json.dump(personOBJ, personJSONFile, indent=4)


# JSON File Read -> Python Object -> JSON String

with open("person.json", "r") as personOBJFile:
    personOBJ = json.load(personOBJFile)
    print(personOBJ['age'])


##########python moduel##############
from calendar import day_name
for day in day_name:
    print(day)

#create a new pyhton file , there define some methode , and use by importing them

################ ####################
