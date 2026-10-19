
# Module 1: Introduction to Python

# 1. Variables
name = "Nikita"
age = 19

print("Welcome to Python!")
print("Name:", name)
print("Age:", age)

# 2. Basic calculations
a = 10
b = 20

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# 3. List
topics = ["Python", "Artificial Intelligence", "Machine Learning"]

print("\nTopics to Learn:")
for topic in topics:
    print(topic)

# 4. Conditional statement
marks = 75

if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

# 5. Function
def add_numbers(x, y):
    return x + y

result = add_numbers(15, 25)
print("Function Result:", result)
