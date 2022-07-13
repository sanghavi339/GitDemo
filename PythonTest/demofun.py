import datetime

# Functions without Arguments
import time


def my_functions():
    #print("This is my First function Example")
    det = datetime.datetime.now()
    print(det)
my_functions()


# Functions with Arguments
def test_function(name,age):
    print(name + " " + age)


test_function("Jay Sanghavi", "28")

# Arbitrary Arguments, *args
def demoart(*name):
    print("The Child Name is " + name[0])
    print("The Child Name is " + name[1])
    print("The Child Name is " + name[2])
demoart("Ronak","JAY", "Ravi")

print("************************** New Out put****************************")


def txtname():

    print("Addition, Subtratcion, Multiplication and Division of Two Number")

txtname()

def Addintegeres(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

Addintegeres(15,5)

