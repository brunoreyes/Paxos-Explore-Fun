msg = "Hello World"
print(msg)

# end python file with .py
# we double click or right click and go to run python file in terminal
# variableName = 'whatever you want in the variable'

bob = 'a tall man'
print(bob)
print(bob[2:6])
# using 2:6 gives us 2,3,4,5, python 0 based so 1st number is included and last number is excluded
# giving us 'tall'
# python is an interpreter, that keeps track of variables as it goes
# otherwise use the play button

bobo = 'abcdefghijkl' 
print(bobo[3:6:2])
#[Starting from index 0+#,Ending # that's not considered,# in between ]
#d e
bob = '0123456789'
print(bob[2:6:2])
# so it starts at 0 but 0 isn't considered and it contionusly goes up by 2 until it reaches 6,
# which it doesn't count because it is that last number. So only 2 & 4.
# Leaving out 0(the number it started with) & 6(the number it ended with)

print(bob[8:-1:-1])
# is 8,7,6,5,4,3,2,1,0

bod = '012345678'
for x in range(0, 7, 2):
    print(bod[x])
    # 0,2,4,6

bod = '012345678'
for x in range(0, 7, 2):
    for y in range(1, 6, 1):
        print(bod[x] + bob[y])
    # 0 + 1
    # 0 + 2 = 02
    # 6 + 5 = 65
# because they are strings
    '6' + '5'
# 0
# 2
# 4
# 6
# 01
# 02
# 03
# 04
# 05
# 21
# 22
# 23
# 24
# 25
# 41
# 42
# 43
# 44
# 45
# 61


mylist = []
mylist.append(12)
mylist.append(22)
mylist.append(12)
mylist.append(2)
print(mylist[0]) #prints out 12
print(mylist[1]) #prints out 22
print(mylist[2]) #prints out 12 
print(mylist[3])  #prints out 2

a, b, c, d = 4, 3, 2, 1
print(a + d)  #prints out 5
print(d, c, b, a)  #prints out 1,2,3,4
e, f = '9', '1'
print(e + f)  #prints out 91 bc it's a string concatenation

myString = "Don't worry about apostrophes using double quotations "

myint = 7.3 #prints out 7.3
print(myint)
myfloat = float(myint) #prints out 7.3
print (myfloat)

# change this code
mystring = "hello"
myfloat = float(10.0)
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# prints out: String: hello, Float: 10.000000, Integer: 20

#Arithmetic, python follows the order of operation PEMDAS
# (parentheses, exponents, multiply, divide, add, subtract)

    number = 1 + 2 + 3 / 4.0
    print(number)  #prints out 1+2+(3/4)=3.75
    
    numbertwo = 1 + 2 * 3 / 4
    print(numbertwo)  #prints out (1+2x3)/4 = 2.5

    remainder = 11 % 3
    print(remainder)  #prints out 2 bc 3 goes into 11 3 times, and has a remainder left of 2
    
    # Here we can use exponents or powers
    squared = 7 ** 2  # 49 or (7 * 7)
    cubed = 2 ** 3  # 8 or (2 * 2 * 2)
    guess = 3 ** 4 #81 or (3 * 3 * 3 * 3)
    
print(squared)  #expect 49
print(cubed)  #expect 8
print(guess)  #expect 81

lotsofducks = 'duck ' * 10
print(lotsofducks)

even_numbers = [0,2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7, 9]
all_numbers = even_numbers + odd_numbers
print(all_numbers)  # expect [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]

a, b, c, d, e = 0, 2, 4, 6, 8
f, g, h, i, j = 1, 3, 5, 7, 9
sum = a + b + c + d + e + f + g + h + i + j
print(sum)  #expect 45

print([1, 2, 3] * 3)  #expect [1, 2, 3, 1, 2, 3, 1, 2, 3]
# or multiplying index values within an object multiple times


x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)  # Hello John Doe. Your current balance is $53.44.

#Reverse a string or array
cat = " tac"
print(cat[3:0:-1])
#[Starting from index 0+#,Ending # that's not considered,# in between ]
print(cat)
#3 so if we were to reverse " tac" we would need to start at the end, which is index 3, bc 0,1,2,3
#0 then we would end at index 0, we cant end at -1 bc it doesn't exist
#-1 and we would decrease by 1 until we reached the index 0, and exclude it.


#Fizzbuzz
# Write a program that prints the numbers from 1 to 16. But for multiples of three print “Fizz”
# instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”
#this is 1-16, bc we don't count the ending number
for num in range(1, 16):
    if num % 5 is 0 and num % 3 is 0:
        print("FizzBuzz")  
    elif num % 3 is 0:
        print("Fizz")
    elif num % 5 is 0:
        print("Buzz")
    else:
        print(num)
# Make sure there is proper indentation of else the function won't run
#elif num % 15 is 0:


#so we had to make sure that if the number was divisable by 3 and 5, it would be the first in the list
#and if nothing showed up we would have to print out the number


#Questions like these should be put at the end bc nothing will show after them.

#Leap Year Challenge
year = int(input("Enter a Year to Check if it is a Leap Year:"))
if (year%400 == 0):
    print("%d is a Leap Year" % year)
    #%d is the placeholder for inputted numerical/decimal values
    #%s is the placeholder for inputter string values
#if the year inputted is divided by 4 and the remainder is 0, tell user it's a leap year
elif (year%100 == 0):
       print("%d is not the Leap Year" % year)
#else if the year is divisable by 100 and the remainder is 0, tell the user, it's not a leap year
#so if it is the first one, it just prints the first one, but if it isn't it goes down the list
elif (year%4 == 0):
       print("%d is the Leap Year" % year)
else:
       print("%d is not the Leap Year" % year)
#if none of the top functions are satisfied, then print out it is not a leap year

