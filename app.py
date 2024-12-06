#Variables
#patient_name = 'John Smith'
#age = 20
#isNew_patient = True

#assigning multiple variables
"""
x, y, z = "Orange" , "Pepper" , "Cherry"
print(x)
print(y)
print(z)
"""
"""
fruits = ["Orange" , "Pear" , "Avocado"]
x,y,z = fruits
print(z)
"""

# input function
#name = input("What is your name? ")
#print("Hello " + name)

#type conversion
#birth_year= input("Enter your birth year ")
#age = 2024 - int(birth_year)
#print(age)

#calculator
#first_number = int(input("Enter the first number "))
#Second_number = int(input("Enter the second number "))
#sum = first_number + Second_number
#print(sum)

#strings

#course = "Machine Learning"#
#print(course.upper())#
"""print(course)
print(course.lower())
print(course.find("L"))#prints out the index position

print("Machine" in course )#prints out true"""

#Arithmetic Operations

#print(10 / 5)
#print(-7//3)
#print(7 * 3)
#print( 4 + 5)
#print(10 ** 3)
#print(10 // 3)

#operator precedence

#x = (10 + 3) *2
# print(x)

#comparison operators
# > , < , ===, != , >= <=
#x = 3 > 2
#print(x)

#logical operators
# and , or , not

#if statements
"""
temperature = 10
if temperature > 30 :
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10 :
    print("It's a bit cold")
else :
    print("It's cold")
print("Done")
"""
"""
#conversion exercise
weight = input("Weight: ")

unit= input(" (K)g or (L)bs ")
if unit.upper() == "K" :
    converted = float(weight) / 0.45
    print("Weight in (L)bs : " + str(converted))
else:
    converted = float(weight) * 0.45
    print("Weight in (K)g: " + str(converted))
    
"""

# while loops
"""
i = 1
while i <= 5:
    print(i * "*")
    i = i + 1
"""

#list
#names = ["John", "Bob", "Mosh", "Sam", "Mary"]
#names[0] = "Jon"
#print(names)
#print(names[0:3])
#length of the list
# print(len(names))
#type of list
#print(type(names))
"""
#list objects
numbers = [1, 2, 3, 4]
print(numbers)
#inserting a number at the beginning of the list
numbers.insert(0, -1)
print(numbers)

print(10 in numbers)
print(1 in numbers)
"""

#for loop
"""
numbers = [1, 2, 3,4,5]
for item in numbers :
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
    
"""

# range function is used to generate a sequence of numbers

#numbers = range(5,10)
#for number in numbers:
  #  print(number)



#Tuples are immutable


fruits = ["Mango" , "Guava" , "Cassava"]
#for fruit in fruits:
    #print(fruit, end=" ")

fruits[2] = "Pear"
print(fruits)
