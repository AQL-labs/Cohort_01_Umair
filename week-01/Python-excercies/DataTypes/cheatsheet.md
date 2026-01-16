# 📘 Week 1 – Python Basics Cheat Sheet

This README cheatsheet provides a beginner-friendly overview of core Python concepts.  
It is designed as a quick reference while learning or revising Python fundamentals.

---

## 📝 Comments

Comments are lines of text ignored by the Python interpreter.  
They are used to explain code and improve readability.

```python
# This is a single-line comment
🔗 String Concatenation

String concatenation combines two or more strings.

Syntax
combined_text = text1 + text2

Example
greeting = "Hi"
name = " Alex"
message = greeting + name

🔢 Data Types

Common Python data types include:

Integer (int)

Float (float)

Boolean (bool)

String (str)

Example
age = 25              # Integer
temperature = 36.6    # Float
is_active = True      # Boolean
is_admin = False      # Boolean
username = "Alice"    # String

🔍 Indexing

Indexing allows access to individual characters in a string.
Index values start from 0.

text = "Python"
first_char = text[0]

📏 len()

Returns the number of characters in a string.

Syntax
len(string_name)

Example
word = "Programming"
count = len(word)

🔠 lower()

Converts all characters in a string to lowercase.

title = "WELCOME"
lowercase_title = title.lower()

🖨️ print()

Displays output to the console.

print("Hello, Python")
print(10 + 5)

➗ Python Operators
Arithmetic Operators
Operator	Description
+	Addition
-	Subtraction
*	Multiplication
/	Division (returns float)
//	Floor Division
%	Modulo (remainder)
Example
a = 15
b = 4

add = a + b
sub = a - b
mul = a * b
div = a / b
floor_div = a // b
remainder = a % b

🔄 replace()

Replaces a portion of a string with another value.

sentence = "I like Java"
updated_sentence = sentence.replace("Java", "Python")

✂️ String Slicing

Extracts a portion of a string.

Syntax
substring = string_name[start:end]

Example
language = "Python"
slice_text = language[0:3]

🧩 split()

Splits a string into a list using a delimiter.

data = "apple,banana,orange"
items = data.split(",")

🧹 strip()

Removes leading and trailing whitespace.

text = "   hello world   "
clean_text = text.strip()

🔠 upper()

Converts all characters in a string to uppercase.

city = "delhi"
uppercase_city = city.upper()

🧮 Variable Assignment

Assigns a value to a variable.

Syntax
variable_name = value

Example
student_name = "Rahul"
score = 90

⭐ Additional Crucial Concepts
🔄 Type Conversion (Casting)

Convert one data type into another.

num_str = "100"
num_int = int(num_str)

price = 49
price_str = str(price)

✅ Boolean Expressions

Used for comparisons and conditions.

x = 10
y = 5

result = x > y

📥 User Input

Accepts input from the user.
By default, input is stored as a string.

name = input("Enter your name: ")

📦 Multiple Variable Assignment

Assign multiple values in a single line.

x, y, z = 1, 2, 3

📌 f-Strings (Formatted Strings)

Embed variables directly inside strings.

name = "Sara"
age = 22
info = f"My name is {name} and I am {age} years old."

🎯 Summary

This cheat sheet covers:

Core Python data types

String operations

Arithmetic operators

Input and output

Formatting and type conversion

Ideal for Python beginners as a quick reference or revision guide 🚀