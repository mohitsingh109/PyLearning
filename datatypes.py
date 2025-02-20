#Data Types
a = 10
b = "String"
c = True
d = 4.5

print(a, b, c, d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Type Conversion

# Convert int to string
str_num = str(a)
print("The number is " + str_num)
print(f"The number is {str_num}")

# Convert String to float
float_str = "3.5"
float_val = float(float_str)
print(f"Float value: {float_val}")

# Convert String to int
num_str = "50"
int_val = int(num_str)
print(f"Int value: {int_val}")

print(int(True))  # 1
print(int(False))  # 0

# This will error out
# num = int("Hello")  # it's a wrong ValueError

# Input - it will always give a string value

name = input("Enter your name: ")
print(f"Hello {name}!!!")

age = int(input("Enter your age: "))
print(type(age))