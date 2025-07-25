# Variables and basic data types
name = "Alice"
age = 25
height = 5.6
is_student = True

# Variables and basic data types
print("Hello, " + name + "!")
print(f"You are {age} years old and {height} feet tall.")
print(f"Student status: {is_student}")

# Basic arithmetic operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")


# If-elif-else example
temperature = float(input("Enter current temperature: "))

if temperature > 30:
    print("It's hot outside!")
elif 20 <= temperature <= 30:
    print("The weather is pleasant.")
else:
    print("It's cold outside!")
    
    
# For loop example
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# While loop example
count = 0
print("\nCounting up to 5 with while loop:")
while count < 5:
    count += 1
    print(count)
    
    
# Working with lists
fruits = ["apple", "banana", "cherry", "date"]

print("Original list:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding items
fruits.append("elderberry")
print("After append:", fruits)

# Removing items
fruits.remove("banana")
print("After remove:", fruits)

# Looping through list
print("\nAll fruits:")
for fruit in fruits:
    print(fruit.title())
    
    
# Defining and calling functions
def greet(name):
    return f"Hello, {name}! Welcome to Python."

def add_numbers(a, b):
    return a + b

# Using the functions
print(greet("Bob"))
result = add_numbers(5, 7)
print(f"5 + 7 = {result}")



# Working with dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "occupation": "Developer",
    "hobbies": ["reading", "hiking", "coding"]
}

# Accessing values
print(f"{person['name']} is a {person['occupation']}")
print("Hobbies:")
for hobby in person["hobbies"]:
    print(f"- {hobby}")

# Adding new key-value pair
person["email"] = "alice@example.com"
print("\nUpdated dictionary:", person)



# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a sample file.\n")

# Reading from a file
print("File contents:")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
        
# String methods and formatting
text = "  learn Python programming  "

# String methods
print(f"Original: '{text}'")
print(f"Strip whitespace: '{text.strip()}'")
print(f"Title case: '{text.strip().title()}'")
print(f"Replace 'Python' with 'JavaScript': '{text.replace('Python', 'JavaScript')}'")
print(f"Find 'pro' in string: position {text.find('pro')}")

# Splitting and joining
words = text.strip().split()
print("\nSplit into words:", words)
print("Joined with commas:", ", ".join(words))

# String formatting
price = 19.99
quantity = 3
print(f"\nTotal: ${price * quantity:.2f}")  # Format to 2 decimal places


import random

# Simple number guessing game
secret_number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    
from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Formatted date: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Date arithmetic
one_week_later = now + timedelta(weeks=1)
print(f"One week later: {one_week_later.date()}")

# Parsing dates
date_string = "2023-12-25"
christmas = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Christmas day: {christmas.strftime('%B %d, %Y')}")

# Creating lists with comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares of even numbers
even_squares = [x**2 for x in numbers if x % 2 == 0]
print("Squares of even numbers:", even_squares)

# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(9/5)*temp + 32 for temp in celsius]
print("\nCelsius to Fahrenheit:")
for c, f in zip(celsius, fahrenheit):
    print(f"{c}°C = {f:.1f}°F")
    
# Try-except blocks for error handling
while True:
    try:
        num = int(input("Enter an integer: "))
        reciprocal = 1 / num
        print(f"The reciprocal of {num} is {reciprocal}")
        break
    except ValueError:
        print("That's not an integer! Try again.")
    except ZeroDivisionError:
        print("You can't divide by zero! Try again.")