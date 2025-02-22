# Arithmetic Operator
# +, -, *, /, %, //, **

a = 10
b = 3

print("Addition : ", a + b)  # 13
print("Sub : ", a - b)  # 7
print("Mul : ", a * b)  # 30
print("Div : ", a / b)  # 3.33333333333
print("Floor Div : ", a // b)  # 3
print("Modulus : ", a % b)  # 1
print("Pow : ", a ** b)  # a ^ b if b = 3 (a * a * a)

# Relational Operators (Always return a boolean value)
# ==(Equal), !=(Not Equal), >(gt), <(lt), >=(gteq), <=(lteq)

x = 15
y = 20
print(x == y)  # False
print(x != y)  # True
print(x > y)  # False
print(x < y)  # True
print(x >= y)  # False
print(x <= y)  # True

# Logical Operator
# and, or, not

print("=============Logical Operator=============")

age = 25
has_id = True

print(age > 18 and has_id)  # True and True ==>  # True
print(age < 18 and has_id)  # False and True ==> # False
print(age < 18 or has_id)  # False or True ==> # True
print(not age < 18)  # False ==> True
print(not age > 18)  # True ==> False

# Assignment Operator
# =, +=, -=, *=, /=, //=, %=, **=
print("=============Assignment Operator=============")
x = 10
x += 5  # x + 5  ==> 10 + 5 ==> 15
print(x)

x *= 2  # x * 2 ==> 15 * 2 = 30
print(x)

x -= 10  # x - 10 ==> 30 - 10 ==> 20
print(x)

x //= 5  # x / 5 ==> 20 / 5 ==> 4
print(x)

x **= 2  # x ^ 2 ==> 4 ^ 2 ==> 16
print(x)

# Operator Precedence (Order Of Execution)
# 1) ()
# 2) **
# 3) * //, /, %
# 4) + , -
# 5) > , <, >=, <=, !=
# 6) not
# 7) and
# 8) or
result = 10 + 3 * 2 ** 2

# 2 ** 2 ==> 4
# 10 + 3 * 4
# 10 + 12
# 22

print(result)  # 22

result = 10 / 2 / 2 * 2  # (Left to right)
# 5 / 2 * 2
# 2.5 * 2
# 5.0
print(result)  # 5.0

# short-circuit evaluation

x = 10
y = 50

result = x != 10 and y == 50  # False and (condition skipped) # No
print(result)

result = x == 10 or y == 50 or x > 5 or y < 50  # True or True  # True
print(result)

# Operator Precedence (Order Of Execution)
# 1) ()
# 2) **
# 3) * //, /, %
# 4) + , -
# 5) > , <, >=, <=, !=
# 6) not
# 7) and
# 8) or

exp1 = 2 * 2 - 4 - 2 * 2 * -1
# 4 - 4 + 4
print(exp1)
