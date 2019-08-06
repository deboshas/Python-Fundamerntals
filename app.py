from collections import deque
from array import array
from sys import getsizeof
from timeit import timeit


print('Hello World')
print('*' * 10)
x = 1  # autopep
name = "Rituparna Datta"
print(name)
print(len(name))
print(name[0:-1])
print(name[-1])
print(name[0:3])
print(name[:3])
course_name = "python \nprogramming"
print(course_name)
first = "ritu"
lastname = "datta"
full = f"    {len(first)}{lastname}"
print(full)
print(full.upper())
print(full.lower())
print(full.strip())
print(full.find("datta"))
print("datta" in full)
fruit = "Apple"
print(fruit[1:-1])


temp = 35
if temp > 30:
    print('Temp is above', temp)
    print("isnode id")
elif temp > 40:
    print("It's nice")
else:
    print("done else")
print("done")

# ternary operator

age = 12
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# logical operator
high_income = True
good_Credit = True
Student = False

print("Eligible for loan") if (
    (high_income or good_Credit) and not Student) else print("Not Eligible for Loan")

# if high_income and good_Credit:
# print("Eligible")


# chaning of comaprision operator
age = 30

if 18 <= age <= 35:
    print("Eligible for chaining")
# looping

for number in range(1, 10, 2):
    print("Attempt", number, number * '.')
# for else
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted multiple  times and failed")

# Nested loop
for x in range(5):
    for y in range(3):
        print(f"{x},{y}")

# Iterables
print(type(5))
print(type(range(10)))

for x in "Python":
    print(x)


for x in [1, 2, 3, 4, 5, 6, 7, 898]:
    print(x)


number = 100
while number > 0:
    print(number)
    number //= 2

print("exercise")

no_of_even = 0
for x in range(1, 10):
    if (x % 2 == 0 and x != 1):
        print(x)
        no_of_even += 1

print(f"we have {no_of_even} numbers")


# Functions
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome abord", last_name)


greet("Mosh", "Hamedani")


def get_greeting(name):
    return f"Hi there ,{name}"


print(get_greeting(name="Mosh"))
print(greet("Mosh", "Hamedani"))

# optinal parameters


def increment(number, by=1):
    return number+by


print(increment(5))

# varable no of arggements, tuples


def Multiple(*numbers):  # number  is a tuple
    total = 1
    for x in numbers:
        total *= x
        return total


# save_user(id=1, name="john", title="Snow")


print(Multiple(2, 3, 4, 56, 7))


# def save_user(**user):  # dictionary object
# print(f"{user["id"]} {user["name"]}")


# Fizz_Buzz algo

def Fizz_Buzz(number):

    if(number % 15 == 0):
        return "Fizz_Buzz"
    elif(number % 3 == 0):
        return "Fizz"
    elif(number % 5 == 0):
        return "Buzz"
    else:
        return number


print(Fizz_Buzz(30))


# Lists
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3], [4, 5], [6, 7]]  # matrix reprenstation
zeros = [0]*5
combine = zeros + letters
print(combine)
list1 = list(range(20))
print(list1)

numbers = list(range(20))
print(numbers[::2])  # every alternate value
print(numbers[::-1])  # reverse order print

first, *others, last = numbers  # list unpacking
print(first, last, others)

# loop over list
for index, number in enumerate(numbers):  # enumerate object and unpacking list
    print(index, number)
# Find index
numbers.index(4)
# if 100 in numbers:
# print(numbers.index(100))

# sorting list
print("sorted ist")
numbers.sort(reverse=True)
print(numbers)
print(sorted(numbers, reverse=True))

items = [
    ("Producte1", 10),
    ("Producte2", 7),
    ("Producte3", 5),
    ("Producte4", 9)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
# lambda expression
items.sort(key=lambda item: item[1])
print(items)

# Map function
itemPrices = list(map(lambda item: item[1], items))
for price in itemPrices:
    print(price)

# filtering

itemFilterd = list(filter(lambda item: item[1] >= 10, items))
print(itemFilterd)

# list comprehensions


# zip function
list1 = [10, 20, 30]
list2 = [1, 2, 3]

# [(10,1),(20,2),(30,3)]

print(list(zip(list1, list2)))

# stack

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
print(browsing_session.pop())
print(browsing_session)


# queue
print("queue")
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()  # FIFO operation
print(queue)

# Tuples
print("Tuples")
point = (1, 2)*3
point1 = tuple([2, 3])

print(point)
print(point1)

#point[2] = 200

if 2 in point:
    print("2 in tuple")

# swap two variable usgn one line of code
x = 10
y = 11
print(x, y)
x, y = y, x
print(x, y)


# Arrays,for large number 10,000 or more ,list is not a good option for large data set
arrayVal = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 90])
arrayVal.append(100)


# sets
print("sets")
sets=[1,1,1,1,2,3,45,2,2,2,2]
uniques=set(sets)
print(uniques)

set2={10,23,34}

unionset = uniques | set2
intersectionset = uniques & set2
minusset= uniques -set2


#Dictinoary
print ("Dictionary")
point = dict(x= 1, y= 2)
print(point["x"])
print(point["y"])
point["z"]=10
print(point["z"])

if "a" in point:
    print(point["a"])

#del point["x"]

print("for each in dictinoary")
for key in point:
    print(key,point[key])

for key,value in point.items():
    print(key,value)

print(point)
#del point
#print(point)

#Dictnoary comprehensions
print("Doctinary comprehesnions")
values=[]
#for x in range(5):
    #values.append(x*2)
#comprehensive way,list
values=[x*2  for x in range(5)]
#comprehensive way,Dictinoary
valueDict={x:x*2 for x in range(5)}
print(valueDict)
#generation object for tuple
valueTuple=(x*2  for x in range(5))
print(valueTuple)   

#Big numbers, generator object for big data
print("generator object")
generatorObject=(x*2  for x in range(100000000000000000000000000000000000000000000000000000000000000000000))
print("size of generator object", getsizeof(generatorObject))
#print("length of generated object", len(generatorObject))
#valuelist = [
    #x*2 for x in range(100000000000000000000000000000000000000000000000000000000000000000000)]
#print("size of in memory list", getsizeof(valuelist))
#for x in generatorObject:
    #print (x)


#unpacking operator
print("Unpacked opearator")
packedList=[1,2,3,4,5,6,7]
print(*packedList)

#Data Structure Exercise
print("Get the most repetaed char in the following  string")
sentence="This is  a  common interview question"
countDict = {char: sentence.count(char) for char in sentence}
sortedcountDict = sorted(countDict.items(),key=lambda kv:kv[1],reverse=True)
print(sortedcountDict[0])


#Exceptions

try:
    #file = open("type.py")
    #using statement in c#
    with open("type.py") as file:
        print("file opened")
        file.__exit__()
    age=(int)(input("Age:"))
    #xfactor=age/0 
#catch in c#
except (ValueError) as ex:
    print("You did not enter valid value")
    print(ex,type(ex))

#finally block in c#
finally:
   # file.close()
    print("done")


def calculate_xfacotor(age):
    if(age <= 0):
        raise ValueError("Age cannot be less than 0")
    return age/10


try:
    calculate_xfacotor(-1)
except ValueError as ex:
        pass



#raise  exception on your own,raisign exception is costly,prefer not to raise exception in your own function
code1 ="""def calculate_xfacotor(age):
    if(age<=0):
        raise ValueError("Age cannot be less than 0")
    return age/10

try:
    calculate_xfacotor(-1)
except ValueError as ex:
        pass"""



print("firstcode", timeit(code1, number=10000))


code2= """def calculate_xfacotor(age):
    if(age<=0):
        return 0
    return age/10

try:
    calculate_xfacotor(-1)
except ValueError as ex:
        pass"""

timerequiredforexecution=timeit(code2,number=10000)
print("secondecode",timerequiredforexecution)

# classes-------------------------------------------------------#classes
class Point:
     
        default_color="This is a class  level attribute"
      #constructor ,self is reference to current point object
        def __init__(self,x,y):
            self.x=x
            self.y=y
         #instacne method     
        def draw(self):
            print(f"Point {self.x} ,{self.y}")
        #class level methods
        #@classmethod
        #def zero(class):
            #class(0,0)
        
        #overriding _str_ from base class,magic methods
        def __str__(self):
            return f"{self.x},{self.y}"
        
        def __eq__(self,other):
            return self.x==other.x  and self.y==other.y
        
        def __gt__(self,other):
            return self.x > other.y and self.y> other.y
        def __lt__(self,other):
            return self.x < other.y and self.y <  other.y

        def __add__(self,other):
            return Point(self.x+other.x,self.y+other.y)





#print class level attributes
print(Point.default_color)
point1 = Point(10,12)
point2=Point(1,2)
point3 = point1.__add__(point2)
print(point3)
#point1.draw()



#Custom collection in python

#class TagCloud:

        #def __init__(self):
            #self.tags={}

        #def add(self,tag):
            #self.tags[tag]=













