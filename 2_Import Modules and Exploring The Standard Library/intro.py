
# import my_module as mm
import sys
sys.path.append('/F:/LearningPython/2_Import Modules and Exploring The Standard Library/another')  # Appending the directory containing my_module.py
import my_module




courses = ['History',"Math","Physics",'CompSci']

# index = find_index(courses,'Math')
# print(index)
# print(t)

# print(sys.path)


import random
random_course = random.choice(courses)
print(random_course)

import math
rads = math.radians(90)
print(math.sin(rads))

import datetime
import calendar
today = datetime.datetime.today()
print(today)

print(calendar.isleap(2017))

import os
print(os.getcwd())
print(os.__file__)

import antigravity