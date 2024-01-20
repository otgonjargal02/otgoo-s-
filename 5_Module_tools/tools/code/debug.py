# Useful resources
# https://www.youtube.com/watch?v=w8QHoVam1-I
# https://www.youtube.com/watch?v=6YLMWU-5H9o
# https://www.youtube.com/watch?v=ChuU3NlYRLQ
# https://docs.python.org/3/library/pdb.html
# https://realpython.com/python-debugging-pdb/#using-breakpoints

# debug a function - example

# import pdb
import sys 
sys.path.append("D:\\Documents\\python\\repo\\Introduction_Python\\7_Debug\code")
import help_debug as help

for i in range(100): 
    output = help.func(i)
    # breakpoint()
    print(output)
