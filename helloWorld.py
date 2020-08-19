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

bob = 'abcdefghijkl' 
print(bob[2:6:2])

bob = '0123456789'
print(bob[2:6:2])
# starts at 2 even though 0 index: ends at this number : step
# 2,4 and ignores the end number 6 because it is the end #

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

