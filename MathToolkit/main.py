"""
MATH TOOLKIT
Step1: Create a folder(package) and create multiple .py files with different purpose and build different functions in those
Step2: Create a __init__.py file for storing the importing of each module. This file will be created inside the package
    --> The init file will import all the functions from each of the modules that are required
    --> We can even do without init but in that case, we have to give the whole package.module for importing the module
Step3: Create the main file outside the package. From the package, import the functions necessary and use it for operations
"""

from tools import *

fact = factorial(7)
print("Factorial: ", fact)

gcd_ = gcd(72, 14)
print("GCD:", gcd_)

lcm_ = lcm(72, 14)
print("LCM:", lcm_)

mean_ = mean([2,3,4,5,6,7])
print("Mean:", mean_)

variance_ = variance([2,3,4,5,6,7])
print("Variance:", variance_)

volume_ = volume(2,3,4)
print("Volume:", volume_)