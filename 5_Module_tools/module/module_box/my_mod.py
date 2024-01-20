"""
it is a module with two functions
"""
import numpy as np

def mmod_func(number):
    """
    multiple by two
    """
    return number*2

def mmod_funcA(number):
    """
    multiple by two
    """
    return number*2

print("I am outside")
yy = 10

if __name__ == "__main__":
    print("I am inside")
    input = 18
    res = mmod_funcA(input)
    print(res)
    print(res == 36)
    assert res == input*2

    # https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
    # https://realpython.com/python-main-function/
    # https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    # https://medium.com/python-features/understanding-if-name-main-in-python-a37a3d4ab0c3