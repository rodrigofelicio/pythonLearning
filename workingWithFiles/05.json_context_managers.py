import json


with open('04.friends_json.txt', 'r') as file:
    file_contents = json.load(file) # reads file and turns it to dictionary

print(file_contents)
print(file_contents['friends'][1])

cars = [
    { 'make': 'Ford', 'model': 'Fiesta' },
    { 'make': 'Ford', 'model': 'Focus' },
]

#create a new json file to add cars_json
with open('04.cars_json.txt', 'w') as cars_json_file:
    json.dump(cars, cars_json_file)

#Convert a Strint into a dictionary:
my_json_strint = '[{"name": "Alfa Romeo", "released": 1950}]'
my_car = json.loads(my_json_strint)
print(my_car[0]['name'])
print(my_car)

#In order to work with JSON, 
#consider dictionaries and lists, not tuples.
