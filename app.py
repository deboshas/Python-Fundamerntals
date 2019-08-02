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


def Multiple(*numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(Multiple(2, 3, 4, 56, 7))
