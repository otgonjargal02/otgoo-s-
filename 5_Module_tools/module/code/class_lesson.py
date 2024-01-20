## Class
# \url{https://stackoverflow.com/questions/33072570/when-should-i-be-using-classes-in-python} 
# OOP vs Functional
class Person:
    "This is a person class"
    age    = 20 
    height = 175
    grades = {}

    # method == function
    def greet(self):
        print('Hello')

    def setGrade(self, course, grade):
            self.grades[course] = grade

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)

bold = Person() # instantiation
print(bold.age)
bold.greet()
Person.greet(bold) # can use class name outside
bold.age = 30      # assign value
print(bold.age)

bold.setGrade('math',4)   
bold.setGrade('physics',3) 
bold.getGPA()

# add path
import os
import sys
m_dir = r"D:\\Documents\\python\\repo\\Introduction_Python\6_Functions"
sys.path.append(m_dir + os.sep + 'module_box') # add folder to path
from my_class import *
# alternative
# from my_class import Hotel 

# Instantiation
iHotel = Hotel(150,100,3)
mHotel = Hotel(250,200,5)


print(iHotel.ng)     # number of guest, variable
print(iHotel.getInfo())  # getInfo method
print(iHotel.__hidVar)   # private (hidden) variable with __ prefix
print(iHotel.dispHid())  # see private variable through a method

iHotel.setGuest(380)     # setGuest method
print(iHotel.ng)     # number of guest, variable
print(iHotel.getGuest()) # number of guest, variable

iHotel.setRoom(18)       # setRoom method
iHotel.setHall(2)        # setHall method
print(iHotel.getInfo())  

iBig = bigHotel()      # child class 

print(iBig.ng)     # number of guest, variable
print(iBig.getInfo())  # getInfo method
print(iBig.__hidVar)   # private (hidden) variable with __ prefix
print(iBig.dispHid())  # see private variable through a method

iBig.setGuest(350)     # setGuest method
print(iBig.getGuest())     # number of guest, variable

iBig.setRoom(18)       # setRoom method
iBig.setHall(2)        # setHall method
print(iBig.getInfo())  
print(iBig.getNumber())# total number of all

# Additional example

from class_example import *

my_pol = Polygon(5)
my_pol.dispSides()
my_pol.inputSides()
my_pol.dispSides()

my_tri = Triangle()
my_tri.dispSides()
my_tri.inputSides()
my_tri.dispSides()
my_tri.findArea()
