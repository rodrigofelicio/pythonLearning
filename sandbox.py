########### CHAPTER 02: Python Fundamentals ###########
########################################################

### Getting a User Input in Python
#age = int(input("Enter your age:  "))
#print(f"You have lived for {age * 12} months.")

########################################################

###Booleans and Comparisons in Python
#my_number = 5
#user_number = int(input("Enter a number: "))

#matches = my_number == user_number

#print(f"You got it right: {matches}.")

########################################################

###AND and OR in Python
#age = int(input("Enter your age: "))
#can_learn_programming = age > 7 and age < 150

#print(f"You can learn programming:  {can_learn_programming}. ")

#usually_working = age > 18 or age < 65
#print(f"You can work: {usually_working}. ")

########################################################

###Lists in Python
#friends = ["Finha", "Anderson", "Junior", "Josielen", "Matheus"]
#print(len(friends))

#friends_and_their_ages = [
#    ["Finha", 43],
#    ["Anderson", 40], 
#    ["Junior", 38], 
#    ["Josielen", 36], 
#    ["Matheus", 34]
#]
#print(len(friends_and_their_ages))
#print(friends_and_their_ages[0])

#friends_and_their_ages.append(["Georgia", 42])
#print(len(friends_and_their_ages))
#print(friends_and_their_ages[5])

#friends_and_their_ages.remove(["Georgia", 42])
#print(friends_and_their_ages)

########################################################

###Tuples in Python
#If you don't want modification, use tuples. 
#If you need modification, use lists(append, remove)
#amigos = ("Kevin", "Bob", "Stuart")
#print(amigos)

#friends = amigos + ("Gru", )
#print(friends)

########################################################

###Sets in Python 
#É outra coleção, como list e tuple. 
#{set} não garante ordem dos itens dentro do Set, 
#mas garante que não haja duplicação de elementos ( o que pode ser um problema tb. ex: notas de provas de um aluno ).
#Set permite modificações. Sets são usados para comparação 

#art_friends = {"Rolf", "Anne"}
#science_friends = {"Jen", "Charlie"}

#art_friends.add("Jen")
#print(art_friends)

########################################################

###Advanced Set Operations
#art_friends = {"Rolf", "Anne", "Jen"}
#science_friends = {"Jen", "Charlie"}
#
#art_but_not_science = art_friends.difference(science_friends)
#science_friends_but_not_science = science_friends.difference(art_friends)
#
#print(art_but_not_science)
#print(science_friends_but_not_science)

########################################################

###Length and Sum
#grades = [80, 75, 90, 100]
#
#total = sum(grades)
#number_of_grades = len(grades)
#
#print(total)
#print(number_of_grades)

###Joining a list
#friends = ["Cotta", "Giba", "Renis"]
#print(f"My friends are {friends}.")
#
#separator = ", ".join(friends)
#print(f"My friends are {separator}.")

########################################################

###If Statements in Python
#friend = "Rolf"
#user_name = input("Enter your name: ")

#if user_name == friend:
#    print("Hello, friend!")
#else:
#    print("Hello, stranger!")

#friends_list = ["Cotta", "Finha", "Giba", "Renis"]
#family_list = ["Finha", "Davi", "Georgia", "Mamae", "Papai"]

#if user_name in friends_list:
#    print(f"Hello, friend {user_name}")
#if user_name in friends_list and family_list:
#    print(f"Hello, my family friend {user_name}.")
#if user_name in family_list:
#    print(f"Hello, my family one {user_name}.")
#else:
#    print("Hello stranger!")

###While Loops in Python
#user_input = input("Do you want me to keep going? (yes/no)")
#
#while user_input == "yes":
#    print("Running!")
#    user_input = input("Do you wish to run the program? (yes/no): ")
#    #print(user_input)
#
#print("We stopped running.")

########################################################

###For Loops in Python
#friends = ["Finha", "Zeh", "Nego"]
#
#for friend in friends:
#    print(friend)
#
#students = [
#    {"name": "Rolf", "grade": 90, "cpf": 27669112867},
#    {"name": "Bob", "grade": 78, "cpf": 27669112867},
#    {"name": "Jen", "grade": 100, "cpf": 27669112867},
#    {"name": "Anne", "grade": 80, "cpf": 27669112867}
#]
#
#for student in students:
#    name = student["name"]
#    grade = student["grade"]
#    cpf = student["cpf"]
#    print(f"O estudante {name}, de cpf {cpf}, conseguiu uma nota {grade} na escola.")

########################################################

####Destructuring Syntax
#currencies = 0.8, 1.2
#usd, eur = currencies
#
#friends = [("Rolf", 25), ("Anne", 23)]
#
#for name, age in friends:
#    print(f"{name} is {age} years old.")

########################################################

###Iterating over Dictionaries
#friends_ages = {"Rolf": 25, "Johge": 33, "Jesus": 33, "Rods": 44}
#
#for name, age in friends_ages.items():
#    print(f"{name} is {age} years old.")

###Break and Continue
#cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok", "ok"]

#for status in cars:
#    if status == "faulty":
#        print(f"This car is {status}.")
#        break ### qdo queremos que o programa termine qdo "algo inesperado" ocorre.
#    print(f"This car is {status}. ")
#    print("Shipping new car to customer. ")

#for status in cars:
#    if status == "faulty":  
#        print(f"This car is {status}. Prosseguindo para o próximo carro.")
#        continue ### qdo queremos que o programa avise "algo inesperado", mas também queremos que continue o fluxo
#    print(f"This car is {status}. ")
#    print("Shipping new car to customer. ")

########################################################

###The Else Keyword with Loops
#cars = ["ok", "ok", "ok", "ok", "ok", "ok", "ok"]
#
#for status in cars:
#    if status == "faulty":
#        print(f"This car is {status}.")
#        break
#    print(f"This car is {status}. ")
#    print("Shipping new car to customer. ")
#else: ### usado qdo queremos realizar alguma ação após o loop ser executado completamente
#    print("All cars built successfully. No faulty cars!")

########################################################

###Finding Prime Numbers with For Loops
#for n in range(2, 10):
#    for x in range(2, n):
#        if n % x == 0:
#            print(f"{n} equals {x} * {n//x}")
#            break
#    else:
#        print(f"{n} is a prime number.")

########################################################

###List Slicing in Python

#friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]

#print(friends[:]) -> friends[:] delivers a new list
#print(friends[-1:]) -> backwards in the list

########################################################

###List Comprehension in Python

#numbers = [0, 1, 2, 3, 4]
##WITHOUT List Comprehension
#doubled_numbers = []
#
#for number in numbers:
#    doubled_numbers.append(number * 2)
#print(doubled_numbers)

###WITH List Comprehension
#doubled_numbers = [number * 2 for number in numbers]
#print(doubled_numbers)
#
#strngs = ['a', "a"]
#ma_numbers = ["rodrigo" for txt in strngs]
#print(ma_numbers)
#
#friends_ages = [22, 32, 35, 33]
#age_strings = [f"My friend is {age} years old." for age in friends_ages]
#print(age_strings)
##print(friends_ages)
#
#names = ["Rolf", "Bob", "Jen"]
#lower_names = [name.lower() for name in names]
#print(lower_names)
#
#friend = (input("Enter your friend name: ")).lower()
#friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
#
#friends_lower = [name.lower() for name in friends]
#
#if friend in friends_lower:
#    print(f"{friend.title()} is one of your friends. ")
#else:
#    print("You have no friends here. ")

########################################################

###Comprehensions with Conditional Statements in Python

#ages = [22, 35, 27, 21, 20]
#odds = [age for age in ages if age % 2 == 1]
#print(odds)

#friends = ["Rolf", "ruth", "Jen", "charlie"]
#guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]
#
#friends_lower = set([friend.lower() for friend in friends])
##print(friends_lower)
#
#guests_lower = set([guest.lower() for guest in guests])
##print(guests_lower)
#
#intersec_lower_friends_guests = friends_lower.intersection(guests_lower)
#print(intersec_lower_friends_guests)
#
#present_friends = [
#    name.title()
#    for name in guests
#    if name.lower() in friends_lower
#]
#print(present_friends)

########################################################

###Set and Dictionary Comprehensions

##Set Comprehension
#friends = ["Rolf", "ruth", "Jen", "charlie"]
#guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]
#
#friends_lower = {friend.lower() for friend in friends}
#guests_lower = {guest.lower() for guest in guests}
#
#present_friends = friends_lower.intersection(guests_lower)
#
#present_friends = {name.title() for name in present_friends}
#print(present_friends)

##Dictionary Comprehension
#friends = ["Rolf", "Bob", "Jen", "Anne"]
#time_since_seen = [3, 7, 15, 11]
#
#long_timers = {
#    friends[n]: time_since_seen[n]
#    for n in range(len(friends))
#    if time_since_seen[n] > 5
#}
#
#print(long_timers)

########################################################

###The Zip Function
#friends = ["Rolf", "Bob", "Jen", "Anne"]
#time_since_seen = [3, 7, 15, 11]
#
#long_timers = dict(zip(friends, time_since_seen))
#print(long_timers)

##If you want to zip lists, even with different numbers of elements...
#long_timers = list(zip(friends, time_since_seen, ["dog", "turtle", "starfish", "cat", "swordfish"]))
##Zip function ignores the over number of elements of the list
#print(long_timers)

########################################################

###Functions in Python
#def greet():
#    name = input("Whats your name, kid?")
#    print(f"Hello, {name}!")
#
#greet()

########################################################

###Arguments and Parameters
#def calculate_mpg():
#    car = {
#        "make": "Ford",
#        "model": "Fiesta",
#        "mileage": 23000, 
#        "fuel_consumed": 460
#    }
#
#    mpg = car["mileage"] / car["fuel_consumed"]
#    name = f"{car['make']} {car['model']}"
#    print(f"{name} does {mpg} miles per gallon.")
#
#calculate_mpg()

## Optimizing function
# ARGUMENT: value you pass in to the function
# PARAMETER: variable that accepts a value inside the function

#my_car = {
#    "make": "Ford",
#    "model": "Fiesta",
#    "mileage": 23000, 
#    "fuel_consumed": 460
#}
#
#cars = [
#    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
#    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
#    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
#    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
#]
#
#def calculate_mpg(a_car): #a_car is the parameter
#    mpg = a_car["mileage"] / a_car["fuel_consumed"]
#    name = f"{a_car['make']} {a_car['model']}"
#    print(f"{name} does {mpg} miles per gallon.")
#
#for car in cars:
#    calculate_mpg(car) #my_car is the argument

########################################################

###Functions and Return Values in Python

#cars = [
#    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
#    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
#    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
#    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
#]
#
#def calculate_mpg(a_car): #a_car is the parameter
#    mpg = a_car["mileage"] / a_car["fuel_consumed"]
#    return mpg
## It is a best practice to jump 02 lines between functions
#
#def get_name(a_car):
#    name = f"{a_car['make']} {a_car['model']}"
#    return name
#
#
#def print_car_info(name, mpg):    
#    print(f"{name} does {mpg} miles per gallon.")
#
#
#
#for car in cars:
#    #print_car_info(get_name(car), calculate_mpg(car))
#    name = get_name(car)
#    mpg = calculate_mpg(car)
#
#    print_car_info(name, mpg)

########################################################

###Default Parameter Values
#
#def add(x, y=3):  # y gets a default value, in this case, 3.
#    total = x + y
#    return total
#
#print(add(5, 6))
#
#ATTENTION: print(add(x=5, 2)) IS NOT ALLOWED
# because the argument that doesn't have a name 
# cannot be used after an argument that has a name. 
# This is also applied when defining a function, as well.
# The opposite can be done, though.

########################################################

###Lambda Functions in Python
#Lambda functions are used to get inputs, 
#do a small amount of processing and return outputs.

#this function below....
#def divide(x, y):
#    return x / y
#print(divide(6, 3))

#is the same as this lambda function...
#divide = lambda x, y: x / y
#print(divide(6, 3))

########################################################

###First Class and Higher Order Functions
##FIRST CLASS function
#def greet():
#    print("Hello")
#
#greet #function without "()" is just a reference. We are not asking Python to run it
#      #just as we can refer to a string or a number. Thus, we can actually assign this
#      #function to another variable if we want, as below:
#
#hello = greet #When we do 'hello = greet', now hello is also the greet function
#              #and we can run it. This is what First Class functions mean
#hello()

#Another example of First Class Function:
#def before_and_after(func): #This is a higher order function. A function
#                            #that accepts another function as an argument
#    print("Before...")
#    func()
#    print("After...")
#
#def greet(): #This is the First Class function. It can be passed as argument
#    print("Hello! I am a first class function!")
#
#before_and_after(greet)

#Another example:
#operations = {
#    "average": lambda seq: sum(seq) / len(seq),
#    "total": sum, #the same as lambda seq: sum(seq)
#    "top": max
#}
#
#students = [
#    {"name": "Rolf", "grades": (67, 90, 95, 100)},
#    {"name": "Bob", "grades": (56, 78, 80, 90)},
#    {"name": "Jen", "grades": (98, 90, 95, 99)},
#    {"name": "Anne", "grades": (100, 100, 95, 100)}
#]
#
#for student in students:
#    name = student["name"]
#    grades = student["grades"]
#
#    print(f"Student: {name}")
#    operation = input("Enter 'average', 'total', or 'top':")
#
#    result = operations[operation](grades)
#    print(result)
########################################################

########### CHAPTER 03: Milestone Project 1 ############
########### See the Milestone_1 folder #################
########################################################

########################################################

########### CHAPTER 04: Object-Oriented ################ 
########### Programming with Python ####################
########################################################

###Intro to Object-Oriented Programming with Python
##
#my_student = {
#    'name': 'Rolf Smith',
#    'grades': [70, 88, 90, 99],
#    'average': None #something here
#}
#
#def avg_grade(student):
##    my_sum = 0
##    for grade in my_student['grades']:
##        my_sum = my_sum + grade
##    avg_grade = my_sum / len(my_student['grades'])
##    print(avg_grade)
#    return sum(student['grades']) / len(student['grades'])
#    
#class Student:
#    #self is the empty blank structure object created when the class is instantiated
#    def __init__(self, new_name, new_grades): # Dunder function
#        self.name = new_name # this self.property is being created in the object (self) and it is receiving teh new_name value
#        self.grades = new_grades
#
#    def average(self): #class method
#        return sum(self.grades) / len(self.grades)
#
#student_one = Student('Rolf Smith', [70, 88, 90, 99])

########################################################

### Parameter Naming in Python
#class Movie:
#    def __init__(self, name, year):
#        self.name = name
#        self.year = year

########################################################

### Magic Methods in Python
# Everything is an object in Python
#print('hi'.__class__)
#
#movies = ['Matrix', 'Finding Nemo']
#print(movies.__class__)
#print(len(movies))
#
#class Garage:
#    def __init__(self):
#        self.cars = []
#
#    def __len__(self):
#        return len(self.cars)
#
#    def __getitem__(self, i):
#        return self.cars[i]
#
#    def __repr__(self):
#        return f'<Garage {self.cars}>'
#    
#    #def __str__(self):
#    #    return f'Garage with {len(self)} cars.'
#
#ford = Garage()
#ford.cars.append('Fiesta')
#ford.cars.append('Focus')
#
#print(len(ford))
#print(ford[0]) # Garage.__getitem__(ford,0)
#
#for car in ford:
#    print(car)
#
#print(ford)


########################################################

### Inheritance in Python
#
### The @property Decorator 
#class Student:
#    def __init__(self, name, school):
#        self.name = name
#        self.school = school
#        self.marks = []
#    
#    def average(self):
#        return sum(self.marks) / len(self.marks)
#
#class WorkingStudent(Student):
#    def __init__(self, name, school, salary):
#        super().__init__(name, school)
#        self.salary = salary
#    
#    #There is no action to do, it just takes a value and deliver it. Thus, this could be a property of the object
#    #We can do it by using the @property decorator:
#    @property
#    def weekly_salary(self):
#        return self.salary * 37.5
#
#rolf = WorkingStudent('Rolf', 'MIT', 15.50)
#print(rolf.salary)
#rolf.marks.append(57)
#rolf.marks.append(99)
#print(rolf.average())
##print(rolf.weekly_salary()) #before using the @property decorator
#print(rolf.weekly_salary) #now, using the @property decorator

########################################################

### The @classmethod and @staticmethod Decorators in Python
#
### More @classmethod and @staticmethod Examples

## @classmethod
#class Foo:
#    @classmethod
#    def hi(cls):
#        print(cls.__name__)
#
#my_object = Foo()
#my_object.hi()
#
###@staticmethod 
#class Bar:
#    @staticmethod
#    def hi():
#        print('Hello, I don\'t take parameters.')
#
#another_object = Bar()
#another_object.hi()
#
#class FixedFloat:
#    def __init__(self, amount):
#        self.amount = amount
#    
#    def __repr__(self):
#        return f'<FixedFloat {self.amount:.2f}>'
#    
#    #def from_sum(self, value1, value2): #without the @staticmethod decorator 
#    
#    # Use @staticmethod whenever you know the class will not be inherited by another class.
#    #@staticmethod
#    #def from_sum(value1, value2):
#    #    return FixedFloat(value1 + value2)
#
#    # Use @classmethod whenever you want to use a method that doesn't use 'self'.
#    @classmethod
#    def from_sum(cls, value1, value2):
#        return cls(value1 + value2)
#
##number = FixedFload(18.5746) #before the @staticmethod, 
## we should create an object and then use it to call the from_sum, below:
##new_number = number.from_sum(19.575, 0.789)
#
#new_number = FixedFloat.from_sum(19.575, 0.789)
#print(new_number)
#
#class Euro(FixedFloat):
#    def __init__(self, amount):
#        super().__init__(amount)
#        self.symbol = 'EUR'
#    
#    def __repr__(self):
#        return f'Euro {self.symbol}{self.amount:.2f}>'
#
#
#money = Euro.from_sum(16.758, 9.999)
#print(money)

########################################################

### Raising Errors in Python

#class Car:
#    def __init__(self, make, model):
#        self.make = make
#        self.model = model
#    
#    def __repr__(self):
#        return f'<Car {self.make} {self.model}>'
#
#
#class Garage:
#    def __init__(self):
#        self.cars = []
#
#    def __len__(self):
#        return len(self.cars)
#    
#    def add_car(self, car):
#        #raise NotImplementedError("We can't add cars to the garage yet.")
#        if not isinstance(car, Car):
#            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car`objects.')
#        self.cars.append(car)
#
#
#ford = Garage()
#car = Car('Ford', 'Fiesta')
##ford.add_car('Fiesta')
#ford.add_car(car)
#print(len(ford))

########################################################

### Creating Erros in Python
#
#"""
#    This is a multi-line string that is used as DocString. 
#    It can be used to add info about modules, classes, methods, or functions in order to create documentation
#"""
#class MyCustomError(TypeError):
#    """
#        This is an example of Class Docstring Documentation
#    """    
#    def __init__(self, message, code):
#        super().__init__(f'Error code {code}: {message}')
#        self.code = code
#
#err = MyCustomError('An error happened.', 500)
#print(err.__doc__)
#
##raise MyCustomError('OUCH! An error happened.', 500)
#
##multi-line strings """"
##print("""
##      This is a multi-line string
##""")

########################################################

### Dealing with Python Errors
#
#class User:
#    def __init__(self, name, engagement):
#        self.name = name
#        self.engagement_metrics = engagement
#        self.score = 0
#    
#    def __repr__(self):
#        return f'<User  {self.name}>'
#
#def get_user_score(user):
#    try:
#        return perform_calculation(user.engagement_metrics)
#    except KeyError:
#        print('Incorrect values provided to our calculation function.')
#        raise # it must be inside the except block of code
#
#def perform_calculation(metrics):
#    return metrics['clicks'] * 5 + metrics['hits'] * 2
#
#def send_engagement_notification(user):
#    print(f'Notification sent to {user}.')
#
#def email_engaged_user(user):
#    try:
#        user.score = perform_calculation(user.engagement_metrics)
#    except KeyError:
#        print('Incorrect values provided to our calculation function.')
#    else:
#        if user.score > 500:
#            send_engagement_notification(user)
#
#
#my_user = User('Rolf', {'clicks': 61, 'hits': 100})
#get_user_score(my_user)
#email_engaged_user(my_user)


#########################################################################
########### CHAPTER 09: Advanced Built-in Functions in Python ###########
#########################################################################

#########################################################################
### Generators in Python
#########################################################################
#
#
# Generators function: It is a function that "remembers" the state it
# is in between executions. Generators are used because when we have a list of 
# elements and need to perform some operation over each one, we don't need
# all the elements at once, we need them one by one. This is what generators
# are used for. Instead of having the entire list of elements, the generator 
# gives us the first element of the list without store all the elements of it
# in the memory. The next time we call the generator, it will "remember" the
# element that it gave us last, and it will know to give us the second one
# and so forth. It never stores the list in memory.

#def hundred_numbers():
#    nums = []
#    i = 0
#    while i < 100:
#        nums.append(i)
#        i += 1
#    return nums

#print(hundred_numbers())
#print([x * 2 for x in hundred_numbers()])

# Generator Function Example
#def hundred_numbers():
#    i = 0
#    while i < 100:
#        yield i
#        i += 1
#        
##print(hundred_numbers())
#g = hundred_numbers()
#print(next(g))
#print(next(g))
#print(list(g))

#
#########################################################################
### Python Generator Classes and Iterators
#########################################################################
#
#

# A class that implements a dunder method __next__ is a Generator.
# All objects that have this Dunder 'next' method are called iterators.
# On the other hand, we can have iterators that are not generators, that don't generate numbers,
# like the FirstHundredIterator object, below.
#class FirstHundredGenerator:
#    def __init__(self):
#        self.number = 0
#    
#    def __next__(self):
#        if self.number < 100:
#            current = self.number
#            self.number += 1
#            return current
#        else:
#            raise StopIteration()
#
#my_gen = FirstHundredGenerator()
#print(my_gen.number)
#next(my_gen)
#print(my_gen.number)
#
#class FirstHundredIterator:
#    def __init__(self):
#        self.numbers = [1, 2, 3, 4, 5]
#        self.i = 0
#    
#    def __next__(self):
#        if self.i < len(self.numbers):
#            current = self.numbers[self.i]
#            self.i += 1
#            return current
#        else:
#            raise StopIteration()
        
#
#########################################################################
### Iterables in Python
#########################################################################
#
#

# This class is a generator (__next__) AND an iterable (__iter__)
#class FirstHundredGenerator:
#    def __init__(self):
#        self.number = 0
#    
#    def __next__(self):
#        if self.number < 100:
#            current = self.number
#            self.number += 1
#            return current
#        else:
#            raise StopIteration()
#        
#    def __init__(self):
#        return self
#    
#    
## This is also an iterable, wich is defined by __len__ and __getitem__ dunder methods
## this is another way of defining an iterable in Python
#class AnotherIterable:
#    def __init__(self):
#        self.cars = ['Fiesta', 'Focus']
#        
#    def __len__(self):
#        return len(self.cars)
#    
#    def __getitem__(self, i):
#        return self.cars[i]
#    
#for car in AnotherIterable():
#    print(car)
#    
### OBS: Iterator - used to get the next value
###      Iterable - used to go over all the values of an iterator
        
#
#########################################################################
### The Filter() Function in Python
#########################################################################
#
#

#def starts_with_r(friend):
#    return friend.startswith('R')

#friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
##start_with_r = filter(starts_with_r, friends) # arg 1: function that returns True/False
##print(next(start_with_r))
##print(next(start_with_r))
##print(next(start_with_r))
#
##another way of using filter, now with a lambda function
#start_with_r = filter(lambda friend: friend.startswith('R'), friends) 
##the filter function above is the same as this generator comprehension below:
#another_starts_with_r = (f for f in friends if f.startswith('R'))
#
##This function below is identical to the functions presented above:
#def my_custom_filter(func, iterable):
#    for i in iterable:
#        if func(i):
#            yield i
#
#start_with_r = my_custom_filter(lambda friend: friend.startswith('R'), friends) 

        
#
#########################################################################
### The Map() Function in Python
#########################################################################
#
#

#friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
#start_with_r = filter(lambda friend: friend.startswith('R'), friends)

#another_starts_with_r = (f for f in friends if f.startswith('R'))

# When the people in our team are accustomed to using 'map'.
#friends_lower = map(lambda x: x.lower(), friends)

# If we need all the values to be in a list, then we can do this list comprehension below
#friends_lower = [friend.lower for friend in friends]

# The generator comprehension is the most used and recommended approach 
# in comparison with the two above ones
#friends_lower = (friends_lower for f in friends)

#print(next(friends_lower))

#class User:
#    def __init__(self, username, password):
#        self.username = username
#        self.password = password
#
#    @classmethod
#    def from_dict(cls, data):
#        return cls(data['username'], data['password'])
    
#users = [
#    { 'username': 'rolf', 'password': '123' }, 
#    { 'username': 'tecladoisawesome', 'password': 'youaretoo' }
#]

#users = [User.from_dict(user) for user in users]
#users = map(User.from_dict, users)

#
#########################################################################
### The Any() and All() Functions in Python
#########################################################################
#
#

#friends = [
#    {
#        'name': 'Rolf',
#        'location': 'Washington'
#    },
#    {
#        'name': 'Anna',
#        'location': 'San Francisco',
#    },
#    {
#        'name': 'Charlie',
#        'location': 'San Francisco'
#    },
#    {
#        'name': 'Jose',
#        'location': 'San Francisco'
#    }
#]

#your_location = input('Where are you right now? ')
#friends_nearby = [ friend for friend in friends if friend['location'] == your_location ]

#if any(friends_nearby): # checks if ANY value is truthy. Returns True if there's at least one or false, if empty
#    print('You are not alone!')
#else:
#    print('No one near you!')

#print(all([0, 1, 2, 3, 4, 5])) # checks if ALL values are true. Returns False if any is not.
    
#""" 
#* Here are some values that evaluate to false
#* 0
#* None
#* [], (), {}
#* False
#"""
#print(bool([]))

#
#########################################################################
### Mutability in Python
#########################################################################
#
#

#friends_last_seen = {
#    'Rolf': 31,
#    'Jen': 1,
#    'Anne': 7
#}
#print(id(friends_last_seen))

#another_variable = friends_last_seen
#print(id(another_variable)) #same memory address of friends_last_seen 

# same content as the previous "friends_last_seen" function, but different dictionary
# thus, different memory address, different objects.
#friends_last_seen = { 
#    'Rolf': 31,
#    'Jen': 1,
#    'Anne': 7
#}
#print(id(friends_last_seen))

# At the code line below, although we change the content of the dictionary, 
# we change the object content, we are not creating a new one.
# 
# Under the hood, Python is doing this:
# friends_last_seen.__setitem__(self, 'Rolf')
#friends_last_seen['Rolf'] = 0 
#print(id(friends_last_seen))

#On the other hand...
#my_int = 5
#print(id(my_int))

#my_int = my_int + 1
## The print function below is going to present a different memory address to my_int 
## because integers are immutable
#print(id(my_int)) 


#Lists are mutable:
#friends = ['Rolf', 'Jose']
#print(id(friends)) # a memory address

#friends.append('Jordan')
# Below we have the same memory address as above. 
# We changed the list, we did not create a new objec
#print(id(friends))

#""""
#* Immutable types in python:
#* integers -> all functions return new int objects
#* floats
#* strings
#* tuples
#"""

#
#########################################################################
### Argument Mutability in Python
#########################################################################
#
#

#an example
#friends_last_seen = { 
#    'Rolf': 31,
#    'Jen': 1,
#    'Anne': 7
#}

#def see_friend(friends, name):
#    friends[name] = 0
#
#
#see_friend(friends_last_seen, 'Rolf')
#print(friends_last_seen['Rolf'])
#
#########################
#another example
#age = 20
#
#def increase_age(current_age):
#    print(f' The value of current_age is {current_age}') # this is going to print 20
#    current_age = current_age + 1 # this curent_age now is 21, a different integer object than 20
#    print(f' Now, the value of current_age is {current_age}')# this is going to print 21, not 20


#print(id(age))
#increase_age(age) 
#print(id(age))

#########################
#one more example
primes = [2, 3, 5]
print(id(primes))
print(primes)


primes += [7, 11] # Python is doing this:  primes = primes.__iadd__([7, 11])
primes = primes + [7, 11] # Python is doing this: primes = primes.__add__([7, 11])
print(id(primes))
print(primes)
