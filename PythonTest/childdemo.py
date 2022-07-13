from oopsdemo import Calculator

class childimp(Calculator):

    secondage = 28

    def __init__(self):

        return self.secondage + self.summation()

    def getcopleteddata(self):
        return self.secondage + self.Age + self.summation()



obj = childimp()
print(obj.summation())
print(obj.getcopleteddata())


