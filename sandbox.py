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
#primes = [2, 3, 5]
#print(id(primes))
#print(primes)


#primes += [7, 11] # Python is doing this:  primes = primes.__iadd__([7, 11])
#primes = primes + [7, 11] # Python is doing this: primes = primes.__add__([7, 11])
#print(id(primes))
#print(primes)

#
#########################################################################
### Default Values for Parameters
#########################################################################
#
#

#accounts global dictionary 
#accounts = {
#    'checking': 1958.00,
#    'savings': 3695.50
#}

#If we do not pass a account name to the function call, it will 
#use the 'checking' account as default in order to process the amount
#in the accounts dictionary
# Another way of writing the default value of a function:
# def add_balance(amount, name='checking')
# the argument that has a default value must follow the argument that doesn't have it
#def add_balance(amount: float, name: str = 'checking') -> float:
#    """ Function to update the balance of an account and return the new balance. """
#    accounts[name] += amount
#    return accounts[name]    


##add_balance(500.00, 'savings')
#add_balance(500.00) # this will use the default name value ('checking')
#print(accounts['checking'])

#
#########################################################################
### Mutable Default Arguments
#########################################################################
#
# THIS IS WHAT WE WANT TO AVOID!!
#
#def create_account(name: str, holder: str, account_holders: list = []):
#    #print(id(account_holders))
#    account_holders.append(holder)
#    
#    return {
#        'name': name,
#        'main_account_holder': holder,
#        'account_holders': account_holders
#    }
#    
#a1 = create_account('checking', 'Rolf')
#a2 = create_account('savings', 'Jen')
#
#print output: 
#{'name': 'savings', 'main_account_holder': 'Jen', 'account_holders': ['Rolf', 'Jen']}
# this ('account_holders': ['Rolf', 'Jen']) happens because the default argument for the
# 'create_account' function gets evaluated when the function is defined, not when the function
# is called. So the list argument and what it points to, by default, 
# is the empty list object ( [] ). So the empty list object gets created when the function gets
# created, not when the function is called.
#print(a2)  

#Solving this empty list problem: 02 possibilities:
#
#01 - do not pass a default argument:
#Function definition ->  def create_account(name: str, holder: str, account_holders: list):
#function call with no default argument list -> create_account('checking', 'Rolf', [])
#
#02 - do not make account_holders a list, but make it equal to None:
#Function definition -> def create_account(name: str, holder: str, account_holders = None):
#Function implementation change:
#def create_account(name: str, holder: str, account_holders: list = []):
#   if not account_holders:
#       account_holders = []
#
#    account_holders.append(holder)
#    
#    return {
#        'name': name,
#        'main_account_holder': holder,
#        'account_holders': account_holders
#    }
#function call with argument as None -> create_account('checking', 'Rolf') , OR
#function call with argument as None, but with a Default Argument in the call:
#create_account('checking', 'Rolf', ['Johge'])


#
#########################################################################
### Argument Unpacking in Python
#########################################################################
#
#
#
#accounts = {
#    'checking': 1958.00,
#    'savings': 3695.50
#}
#
#def add_balance(amount: float, name: str) -> float:
#    accounts[name] += amount
#    return accounts[name]
#
#
#transactions = [
#    (-180.67, 'checking'),
#    (-220.00, 'checking'),
#    (220.00, 'savings'),
#    (-15.70, 'checking'),
#    (-23.90, 'checking'),            
#    (-13.00, 'checking'),            
#    (1579.50, 'checking'),            
#    (-600.50, 'checking'),            
#    (600.50, 'savings'),
#]
#
#for t in transactions:
#    #add_balance(t[0], t[1]) #instead of this, python gives us a shorthand:
#    add_balance(*t) # the '*t' unpacks iterable into arguments
#    
#    #named arguments:
#    #add_balance(amount=t[0], name=t[1])
#    #another unpacking: '**' - it unpacks a dictionary as named arguments to a function
#    
#class User:
#    def __init__(self, username, password):
#        self.username = username
#        self.password = password
#        
## imagine these users are coming from a database...
#users = [
#    { 'username': 'rolf', 'password': '123'},
#    { 'username': 'tecladoisawesome', 'password': 'youaretoo'}
#]
#
##user_objects = [User(username=data['username'], password=data['password']) for data in users]
## instead of doing the line above, we can do the line below (a named arguments/dictionary unpacking (**data)).
#user_objects = [User(**data) for data in users]
#
#users = [
#    ('rolf', '123'),
#    ('tecladoisawesome', 'youaretoo')
#]
#
##user_objects = [User(*data) for data in users]


#
#########################################################################
### Some Interesting Python Collections
#########################################################################
#
#

"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

#from collections import Counter
#
#device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]
#
#temperature_counter = Counter(device_temperatures)
#print(temperature_counter[14.5])
#
###################
#from collections import defaultdict
#
#coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]
#
#alma_maters = defaultdict(list)
#
#for coworker, place in coworkers:
#    alma_maters[coworker].append(place)
#    
##In order to handle errors, consider 'None' for the default_factory (below). 
##It will raise a traceback error in case a value is not in tuple list, 
##while 'int' will raise the int number so it can be handled in a exception block 
#alma_maters.default_factory = None 
#   
#print(alma_maters['Rolf'])
#print(alma_maters['Anne'])

###################
#from collections import defaultdict
#my_company = 'Teclado'
#
#coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
#other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]
#
#coworker_companies = defaultdict(lambda: my_company)
#
#for coworker in coworkers:
#    coworker_companies[coworker]
#
#for person, company in other_coworkers:
#    coworker_companies[person] = company
#
##print(coworker_companies[coworkers[1]])
##print(coworker_companies['Rolf'])
#print(coworker_companies)


###################
#from collections import OrderedDict
#
#o = OrderedDict()
#o['Rolf'] = 6
#o['Jose'] = 12
#o['Jen'] = 3
#print(o)
#
#o.move_to_end('Rolf')
#o.move_to_end('Jen', last=False)
#print(o)
#
#o.popitem() #remove an item from the end of the dict/list
#print(o)

###################
#from collections import namedtuple
#
#account = ('checking', 1850.90)
#
##print(account[0]) # name
##print(account[1]) # balance
#
#Account = namedtuple('Account', ['name', 'balance'])
#account = Account('checking', balance=1850.90)
##account = Account('checking', 1850.90) # positioning arg('checking') and named arg ('balance')
#print(account.name)
#print(account)
#
#accountNamedTuple = Account(*account)
#print(accountNamedTuple._asdict()['balance']) #1850.90

###################
#
#from collections import deque
#
#friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
#friends.append('Jose')
#friends.appendleft('Anthony')
#print(friends)
#
#friends.pop()
#friends.popleft()
#print(friends)

#
#########################################################################
### Timezones - Dates and Time in Python
#########################################################################
#
#

#from datetime import datetime, timezone, timedelta
#
#print(datetime.now()) # naive time (don't know the timezone)
##Our program should always work with UTC time. Then, when presenting it to the user, convert it.
#print(datetime.now(timezone.utc))  
#
#today = datetime.now(timezone.utc)
#tomorrow = today + timedelta(days=1)
#
#print(today)
#print(tomorrow)
#
#print(today.strftime('%d-%m-%Y %H:%M'))
#
#user_date = input('Enter the date in YYYY-mm-dd format: ')
#user_date = datetime.strptime(user_date, '%Y-%m-%d') #strint parse time
#print(user_date)

#
#########################################################################
### Timing Your Code in Python
#########################################################################
#
#
#
#import time
#
#def measure_runtime(func):
#    start = time.time()
#    func()
#    end = time.time()
#    print(end - start)
#    
#def powers(limit):
#    return [x**2 for x in range(limit)]
#
#measure_runtime(lambda: powers(5000000))
#
#import timeit
#print(timeit.timeit("[x**2 for x in range(10)]"))
#print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))

#
#########################################################################
### Regular Expressions (RegEx) in Python
#########################################################################
#
#

#import re #regular expression module

## Example 01
#email = 'jose@tecladocode.com'
#expression = '[a-z\.]+'
#
#matches = re.findall(expression, email)
#print(matches)
#
#name = matches[0]
#domain = matches[1]
#domain = f'{matches[1]}.{matches[2]}'
#
#print(name)
#print(domain)
##############
## Example 02
#
#email = 'jose@tecladocode.com'
#parts = email.split('@')
#
#name = parts[0]
#domain = parts[1]
#
#print(parts)
#print(name)
#print(domain)
##############
## Example 03
#price = 'Price: $189.50'
#expression = 'Price: \$([0-9,]*\.[0-9]*)'
#
#matches = re.search(expression, price)
#print(matches.group(0))
#print(matches.group(1))
#
#price_without_comma = matches.group(1).replace(',', '')
#price_number = float(price_without_comma)
#print(price_number)

#
#########################################################################
### Introduction to Logging in Python
#########################################################################
#
#
#
#"""
#LOGGING LEVELS:
#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL
#"""
#
#import logging
#
#logger = logging.getLogger('test_logger')
## logging pattern configuration. 
#logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG) # 'the lowest level expected'
#logger.info('This will not show up')
#logger.warning('This will.')
#logger.debug('This is a debug message.')
#logger.critical('A critical error occurred.')


#
#########################################################################
### Logging to a File and Other Features
#########################################################################
#
#
#import logging
#
#logging.basicConfig(
#    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#    datefmt='%d-%m-%Y %H:%M:%S',
#    level=logging.DEBUG,
#    filename='logs.txt'
#)
#logger = logging.getLogger('test_logger')
##logger = logging.getLogger(__name__)
##logger = logging.getLogger('books')
##logger = logging.getLogger('books.database') #child logger
#
#logger.info('This will not show up.')
#logger.warning('This will.')
#logger.debug('This is a debug message.')
#logger.critical('A critical error occurred.')


#
#########################################################################
### Higher-order Functions in Python
#########################################################################
#
#
#
#def greet():
#    print("Hello")
#
#def before_and_after(func):
#    print("Before...")
#    func()
#    print("After...")
#    
##before_and_after(lambda: 5)
#before_and_after(greet)
#
#movies = [
#    {"name": "The Matrix", "director": "Wachowski"},
#    {"name": "A Beautiful Day in the Neighborhood", "director": "Heller"},
#    {"name": "The Irishman", "director": "Scorsese"},
#    {"name": "Klaus", "director": "Pablos"}, 
#    {"name": "1917", "director": "Mendes"},
#]      
#
#def find_movie(expected, finder):
#    found = []
#    for movie in movies:
#        if finder(movie) == expected:
#            found.append(movie)
#    return found
#
#find_by = input("What property are we searching by? ")
#looking_for = input("What are you looking for? ")
#
#movie = find_movie(looking_for, lambda movie: movie[find_by])
#print(movie or 'No movies found.')