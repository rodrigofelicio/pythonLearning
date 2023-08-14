import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file) # reads file and turns it to dictionary

file.close()

print(file_contents)
print(file_contents['friends'][1])

cars = [
    { 'make': 'Ford', 'model': 'Fiesta' },
    { 'make': 'Ford', 'model': 'Focus' },
]

#create a new json file to add cars_json
cars_json_file = open('cars_json.txt', 'w')
json.dump(cars, cars_json_file)
cars_json_file.close()

#Convert a Strint into a dictionary:
my_json_strint = '[{"name": "Alfa Romeo", "released": 1950}]'
my_car = json.loads(my_json_strint)
print(my_car[0]['name'])
print(my_car)

#In order to work with JSON, 
#consider dictionaries and lists, not tuples.
