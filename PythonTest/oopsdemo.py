# self keyword is mandatory for calling variables names into method.

class Calculator:
    name = "Jay Sanghavi"
    Age = 28
    mobile = 8141164339

    # This is Defualt Constructor
    def __init__(self, a, b):
        self. firstnumber = a
        self. secondnumber = b
        print("This Constructor is called defualt when class object is called.")

    def getdata(self):
        print("run get data method in calculator class")


    def summation(self):
        #print("Test Summation Function")
        #print(self.firstnumber + self.secondnumber)
        return self.firstnumber + self.secondnumber + self.Age

    def multiplication(self):
        return self.firstnumber * self.secondnumber * self.Age

    def subtraction(self):
        return self.firstnumber / self.secondnumber / self.Age




obj = Calculator(5, 9)
#print(obj.name)
#print(obj.Age)
#print(obj.mobile)
obj.getdata()
print(obj.summation())
print(obj.multiplication())
print(obj.subtraction())



