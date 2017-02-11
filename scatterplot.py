'''
histogram_age_income.py 
Daniel Protacio, Alex Jwijat

(c) 2014 Project Lead The Way
'''

import random
import matplotlib.pyplot as plt
import numpy as np
import os.path

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'sleeptogpa.csv')
datafile = open(filename,'r')
data = datafile.readlines()
gpas=[]
sleeps=[]


for line in data[1:30]:
    
    sleep, gpa = line.split(',') 
    gpas.append(float(gpa))
    sleeps.append(float(sleep))
    

# Scatter plot
fig_sizes, ax_sizes = plt.subplots(1, 1)
ax_sizes.set_xlabel('Amount of Sleep')
ax_sizes.set_ylabel('GPA')
ax_sizes.set_title('How Amount of Sleep Affects GPA')

N=30
x = sleeps
y = gpas
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2

plt.scatter (x,y)
plt.show()

