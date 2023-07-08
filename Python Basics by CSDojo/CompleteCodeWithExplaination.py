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
f = 8
if e < f:
    print(" e less than f")
elif e == f:  # here == means equal to, = in python means assigning operation
    print(" e is equal to f")
else:
    print("nothing")
