#%% Functions
import pandas as pd
import numpy as np 

def myFunc(myInput):
    # Basic function
    """
    This function multiplies a number by two
    Input:  [list, tuple, dictionary, pd dataframe] 200*50*30 (country*variable*year)
    Output: a number [200*50*30*5 (country*variable*year*indicator)]

    Copyright: Sugarkhuu Radnaa, 2021
    """
    print("Hi")
    twice = myInput * 2
    return twice # void


def two_times(number):
    # Function name is good when short, meaningful and easy to read
    # docstring
    """ 
    multiply by two
    input: a number
    output: a number
    """
    twice = number*2
    
    return twice 

    # Prototype docstring
def my_function(salary, age):
    """
    
    Purpose of the function is to estimate expected salary in two years

    Parameters
    ----------
    salary : float
        salary of an employee
    age : int
        age of an employee

    Returns
    -------
    sal2: float
        twice the first input.


    copyright @Py4Econ
    
    """
    age1 = age*2
    return salary*2


def two_three_times_tuple(number):
    # multiple output as tuple
    """
    multiply by two and three
    """
    first = number*2
    second = number*3
    return first, second
    # return number*2, number*3 # tuple

def two_three_times_list(number):
    # multiple output as list
    """
    multiply by two and three
    return list
    """
    #return number*2, number*3 # tuple
    return [number*2, number*3] # list

def aging(age=25, year = 93):
    # keyword default arguments
    """
    """
    
    print("Age is {}".format(age))
    age_10 = age - 10
    year_10 = year + 10
    return age_10, year_10

def aging1(year,age=25):
    # positional and default (keyword) arguments
    """
    """
    age_10 = age + 10
    year_10 = year + 10
    return age_10, year_10

# error
def aging1(age=25, year):
    # positional (keyword) and default arguments
    """
    """
    age_10 = age + 10
    year_10 = year + 10
    return age_10, year_10

def aging2(year, year1, age=25,avar = 17):
    # positional and keyword arguments
    """
    """    
    print("Age is %d and avar is %d. Name is %s" % (age,avar,"Bat"))
    
    age_10 = age + 10
    year_10 = year + 10
    return age_10, year_10, year1 +10, avar-5

#*optional inputs *yuchgjbln
def aging_args(*args):
    #optional (or arbitrary) positional arguments
    print("hi")
    if len(args) >= 3:
        print(args[2])
    elif len(args) > 0:
        print(args[0])
    else:
        print('No optional argument. Stopping.')

# def aging_args2(year=3, year1, age=25,avar = 17,*args): SyntaxError: non-default argument follows default argument
def aging_args2(year, year1, age=25,avar = 17, *fun):   # (year, year1, *fun, age=25,avar = 17):
    #optional (or arbitrary) positional arguments
    print("hi")
    print(fun[0])
    print(fun[2])
    
def aging_kwargs(**kwargs):
    #optional (or arbitrary) keyword arguments
    print("hi")
    print(kwargs)
    print(kwargs['numberChild'])
    print(kwargs['nkeys'])

def aging_kwargs2(**kwargs):
    #optional (or arbitrary) keyword arguments
    print("hi")
    # print(kwargs['numberChild'])
    if 'numberChild' in kwargs.keys():
        print("numberChild exists") 
        print(kwargs['numberChild']*5)
    elif 'nkeys' in kwargs.keys():
        print("use nkeys")
        print(kwargs['nkeys']*5)
    else: 
        print("do nothing with numberChild and nkeys")
    
    return kwargs['nkeys']*5
    
result = myFunc(10)   # basic
print(result)         # print to terminal
print(two_times(150)) # intelligible function name
help(my_function)     # prototype docstring
# print(my_function())  # error: arguments required
print(two_three_times_tuple(15)) # multiple output as tuple
print(two_three_times_list(15))  # multiple output as list
help(two_three_times_list)
print(aging())        # default values will be taken 
print(aging(35,17))   # can overwrite default values
print(aging1(5))      # must assign positional argument
print(aging2())       # error: must assign positional argument
print(aging2(93,95))  # must assign positional argument
print(aging_args(15,25,35)) # any arguments, should be accessed by position
print(aging_args(15))
print(aging_args())
print(aging_args2(85,75,15,25,35,23,25)) # any arguments, should be accessed by position
print(aging_args2(85,75,15,25))
print(aging_kwargs(numberChild = 3, nkeys = 5, muyu_arg = 10)) # any keyword arguments
print(aging_kwargs2(nkeys=5)) # example of any keyword arguments
print(aging_kwargs2(nbold=15)) # example of any keyword arguments


def my_func(order=5):
    
    beleg = 5 # local by default 
    total = beleg + order
    return total



