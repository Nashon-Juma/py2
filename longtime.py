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