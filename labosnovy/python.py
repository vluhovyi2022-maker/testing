a = "text variable"
b = 1
b1 = 1.1

c = ["a", 1, 1.25, "Word", a]

d = {
    "a": "Word",
    "b": 1,
    a: b
}
e = ("a", a)

f = {"ss", a}
print(a)
print(b)
print(b1)
print(c)
print(d)
print(e)
print(f)
#2
print("First constant:", True)
print("Second constant:", False)
print(f"Third constant: {None}")

import sys
help("keywords")
#3
print(abs(-12.5), "is equal to", abs(12.5), "comparison result:", abs(-12.5) == abs(12.5))
print(len("Python"), "length of string")
print(round(3.14159, 2), "rounded value")
#4
for i in range(5):
    print(f"Current number: {i}")
else:
    print("For loop completed!")
#5
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
#6
A = 0
try:
    print("What happens if", 10 / A, "?")
except Exception as e:
    print("Caught an error:", e)
finally:
    print("Finally block executed!")
#7
with open("example.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

with open("example.txt", "r") as f:
    for i, line in enumerate(f):
        print(f"{i}) {line.strip()}")
#8
def greet(name, age):
    return f"My name is {name}, I am {age} years old"
greet_lambda = lambda name, age: f"My name is {name}, I am {age} years old"
print("Regular function:", greet)
print("Lambda function:", greet_lambda)
print("Lambda call:", greet_lambda("Volodymyr", 30))
def get_data():
    return ("Anna", 25)

print("Lambda with unpacked data:", greet_lambda(*get_data()))
