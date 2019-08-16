#    By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Mudit Bengani
# Section: 516
# Assignment: Functions
# Date: 4 December 2018

import numpy as np
import math
import matplotlib.pyplot as plt

# Python Project - Part 1

def part1(txtfile):
    Data = open(txtfile, 'r')
    data = Data.read()
    data = data.split('\n')
    Data.close()
    return data

'''This function opens, reads, splits and closes the file. The returned value are the equations in a list.'''

def trap_int(eqn, lim1, lim2, wid):
    x1 = lim1
    x = x1
    fx1 = eval(eqn)
    x2 = lim1 + wid
    x = x2
    fx2 = eval(eqn)
    intg = ((fx1 + fx2)/2)*(abs(x2-x1))
    ttlintg = intg
    xg = [x1]
    yg = [fx1]
    while x2 < lim2:
        x1 = x2
        x = x1
        fx1 = eval(eqn)
        x2 = x1 + wid
        x = x2
        fx2 = eval(eqn)
        intg = ((fx1 + fx2) / 2) * (abs(x2 - x1))
        ttlintg += intg
        xg.append(x1)
        yg.append(fx1)
    xg.append(x2)
    yg.append(fx2)
    eqn = eqn.replace('math', 'np')
    x = np.linspace(lim1, lim2, 10000)
    y = eval(eqn)
    plt.plot(x, y)
    plt.plot(xg, yg,"rs--")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.suptitle("Python Project Part #1")
    plt.show()
    return ttlintg

'''This function calculates the integration with trapezoids and returns it along with the graphs of the functions.'''

def trap_int_eqn5(eqn, lim1, lim2, wid):
    x1 = lim1
    x = x1
    fx1 = eval(eqn)
    x2 = lim1 + wid
    x = x2
    fx2 = eval(eqn)
    intg = ((fx1 + fx2)/2)*(abs(x2-x1))
    ttlintg = intg
    xg = [x1]
    yg = [fx1]
    while x2 < lim2:
        x1 = x2
        x = x1
        fx1 = eval(eqn)
        x2 = x1 + wid
        x = x2
        fx2 = eval(eqn)
        intg = ((fx1 + fx2) / 2) * (abs(x2 - x1))
        ttlintg += intg
        xg.append(x1)
        yg.append(fx1)
    xg.append(x2)
    yg.append(fx2)
    eqn = eqn.replace('math', 'np')
    # x = np.linspace(lim1, lim2, 10000)
    # y = eval(eqn)
    # plt.plot(x, y)
    plt.plot(xg, yg,"rs--")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.suptitle("Python Project Part #1")
    plt.show()
    return ttlintg

'''This function calculates the integration with trapezoids and returns it along with the graphs of the functions
only for equation 6 as it was a special case. Essentially, the plt.plot(x, y) has been commented out as it is the 
same as plt.plot(xg, yg, "rs--").'''

# Python Project - Part 2

def fileopn(txtfile):
    Data = open(txtfile, 'r')
    data = Data.read()
    data = data.split('\n')
    city = []
    for i in data:
        j = i.split('         ')
        city.append(j[-1])
    Data.close()
    city.pop(-1)
    arrayname = []
    for i in city:
        arrayname.append(float(i))
    arrayname = np.array(arrayname)
    arrayname[arrayname < -98.0] = 0
    return arrayname

'''The function above opens the text file, appends them to arrays and also ignores values like -99.'''

