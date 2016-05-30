__author__ = 'Xavier'

age = 20
if age > 18:
    print("your age is ", age)
    print("adult")
else:
    print("your age is", age)
    print("teenager")

birth = input("birth : ")
if int(birth) < 2000:
    print("00前")
else:
    print("00后")
