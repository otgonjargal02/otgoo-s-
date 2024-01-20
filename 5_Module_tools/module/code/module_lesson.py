

## Module

# importing modules

import pandas as pd  # pd can be pds or whatever you want
import pandas      # then should use pandas.DataFrame not pd.DataFrame
import numpy as np  


import os # operating system functionality is contained
print(os.getcwd()) # current working directory will be printed

# setting main dir is useful
m_dir = r"D:\\Documents\\python\\repo\\Introduction_Python\6_Functions"

# Path
import sys # system parameters
print(sys.path) # all folders in path 
# sys.path.append(r"D:\\Documents\\python\\repo\\Introduction_Python\6_Functions\module")
sys.path.append(m_dir + os.sep + 'module_box') #  os.sep = \ add folder to path m_dir\\module. mdir/module
print(sys.path) # all folders in path 
sys.path.remove(m_dir + os.sep + 'module') # remove folder from path
sys.path.append(m_dir + os.sep + 'module') # add folder to path

## add path permanently
# import site
# site.addsitedir(r'D:\\Documents\\python\\repo\\Introduction_Python\6_Functions\module')
# sys.path.remove(r'D:\\Documents\\python\\repo\\Introduction_Python\\6_Functions\\module') # remove folder from path

# import
import my_mod
print(my_mod.mmod_func(5))

help(my_mod)
del my_mod

import my_mod as mm
print(mm.mmod_func(5))


# import specific function
from my_mod import mmod_funcA as myA
myA(53)

from my_mod import mmod_funcA, mmod_func
mmod_funcA(53)
mmod_func(43)

# import all as system level functions
from my_mod import * 
mmod_funcA(5)
yy

# same with pandas or other packages
from pandas import *
# read_csv()
del pandas


import my_mod
