print("Hello, Python!")
print("My Python environment is working!")
print("Python executable is on D drive.")
name='vina  '
age=38



#f-strings
print(f"my name in {name.strip()} age is {age}")

marks = 90

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")


for i in range(5):
    print(i)

#while loop
i = 0

while i < 5:
    print(f"while {i}")
    i += 1



#logical operation and or not ,>,<,!=,==...
age = 25
salary = 50000
if age >= 18 and salary >= 30000:
    print("Eligible")


def greet(name="User"):
    print(f"Hello {name}")

greet("vinay")
greet()

numbers = [10, 2, 1, 40] #list
print(numbers)
print(numbers[3])

numbers.append(50)
print(numbers)
numbers.insert(1,10.5)
print(numbers)
print(len(numbers))

numbers.remove(10)
print(numbers)

numbers.pop(0)
print(f"after poop {numbers}")
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
print(numbers[1:3])

for number in numbers:
    print(number)

comprehensionNumber = test = [i * 2 for i in range(10)]
print(comprehensionNumber)
print(test)

comprehensionNumber = [i for i in range(10) if i%2==0]
print(comprehensionNumber)

comprehensionNumber = [i*2 for i in range(10) if i%2==0]
print(comprehensionNumber)

numbers = (100,10,30) #tuple
print(numbers)

#numbers[0] = 200 tuple datatype is immutable
print(len(numbers))
#numbers.reverse() no function because tuple is immutable
#numbers.sort() no function because tuple is immutable
#numbers.append(20) no function because tuple is immutable

numbers = {1, 2, 3, 3, 3} #set

print(numbers)

numbers = [1, 2, 2, 3, 4, 4]

unique = set(numbers)
print(numbers)
print(unique)

# set operation
a = {1, 2, 3}
b = {3, 4, 5}

print(f"union {a | b}") #union
print(f"intersion {a & b}") #intersion
print(F"difference {a - b}") #difference 
print(F"difference {b - a}") #difference 

#Dictionary hashmap in java

person = {
    "name": "Vinay",
    "age": 35,
    "city": "Bangalore"
}
print(person)
print(person["name"])

person["salary"] = 100000
print(person)
person["age"] = 36
print(person)
del person["city"]
print(person)
person["noneKey"] = None

if "name" in person:
    print("Found")

if "city" in person:
    print("Found")
else:
    print("not found")

for key, value in person.items():
    print("#")
    print(key, value)
    print("#")
print(f"keys {person.keys()}")
print(f"values {person.values()}")

from collections import Counter

numbers = [1,1,1,2,2, 2, 2, 3, 3, 3]

count = Counter(numbers)

print(count)


from collections import defaultdict

groups = defaultdict(list)

groups["A"].append("Apple")
groups["A"].append("Avocado")
groups["B"].append("Banana")
print(groups)

a="10fjkfl"
b=a
print(type(a))
print(f"{(a)} and {(b)}")
print(f"{id(a)} and {id(b)}")
b=20
print(type(b))
print(f"{id(a)} and {id(b)}")
print(f"{(a)} and {(b)}")

# Create an empty dictionary to hold the variables
my_vars = {}

# Loop 10 times to generate names like var_1, var_2, etc.
for i in range(1, 11):
    my_vars[f"var_{i}"] = f"Value {i}"

# Accessing a specific variable
print(my_vars["var_5"])  # Output: Value 5

print(my_vars)

a="bangalore"
b="mysore"
print(f"{a}-{id(a)} and {b}-{id(b)}")
b="delhi"
c="mysore"

print(f"{c}-{id(c)} and {b}-{id(b)}")