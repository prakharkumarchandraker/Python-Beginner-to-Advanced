print('hello')  # We can print a string with '' quotes.
print('world')  # We can print a string with "" quotes.
print('3')  # We can print a number/integer with "" quotes.
print('3.0')  # We can print a Float value with "" quotes.
# variable
a = 1  # assigns 1 to a, a refers to the value 1
print(a)
b = 2  # assigns 1 to a, a refers to the value 1
print(b)
c = "hello"
d = 2
# Here a will refer to 1 , b will refer to value 2 , c will refer to "hello"
# and d will refer to 2 saved in memory again.
# We can reassign a variable
b = 1
a = 1
b = "hello"
c = a
# c refers to value of a which refers to memory location of 1
a = 2
# if value of a changes, c will still refer to 1
print("value of a = "+str(a))
# We need to convert a to string before printing it because we cannot concatenate String to Integer
print("value of c = "+str(c))

# Swapping Two Variables
a = "Value of a"
b = "Value of b"
print("a=" + a)
print("b=" + b)
temp = a  # temp will have value of a
a = b  # a will now have value of b but value of temp will not change as it still refers to original value of a
b = temp  # value of temp will now be overwritten to b
print("a=" + a)
print("b=" + b)

# if else statement
a = 1
b = 2
if a < b:
    print(" a is less than b")  # This is under if Clause
print("Not sure if a is less than b")  # This is outside of if clause,so it will be printed regardless

c = 3
d = 4
if c < d:
    print("c is less than d")
else:
    print(" c is not less than d")
print("This is outside the if else clause")

e = 5
f = 6
if e < f:
    print("e less than f")
elif e == f:  # here == means equal to, = in python means assigning operation
    print("e is equal to f")
else:
    print("nothing")

# we can also have nested if else
g = 7
h = 8
if g < h:
    print('g is less than h')
else:
    if g == h:
        print("g=h")
    else:
        print("nothing")

"""
Arithmetic operators
/ means divide
* means multiply
** means power
+ means addition
- means subtraction
% means modulus
// means floor division 
 The division operator / in Python returns the exact result of the division operation as a floating-point number
 , while the floor division operator // returns the quotient rounded down to the nearest integer
"""
"""
Assignment Operators
= equal
+= example is x+=3 means x=x+3
-= example is x-=3 means x=x-3
*= example is x*=3 means x=x*3
/= 
//=
%=
**=
&= Performs Bitwise AND on operands and assign value to left operand	a &= b   
|= Performs Bitwise OR on operands and assign value to left operand	a |= b    
^= Performs Bitwise xOR on operands and assign value to left operand	a ^= b    
>>= Performs Bitwise right shift on operands and assign value to left operand	a >>= b     
<<= Performs Bitwise left shift on operands and assign value to left operand	a <<= b
"""
"""
Identity Operators
is  True if the operands are identical 
is not True if the operands are not identical 
"""
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

"""
Membership Operators
in            True if value is found in the sequence
not in        True if value is not found in the sequence
"""
# Python program to illustrate
# not 'in' operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if x not in list:
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if y in list:
    print("y is present in given list")
else:
    print("y is NOT present in given list")


