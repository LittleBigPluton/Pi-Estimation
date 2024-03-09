#!/usr/bin/python3
###############################
#####   Import libraries  #####
###############################

import math
import random

###############################
#####  PI From MC Method  #####
###############################

def MC_PI_calculator (attempts):
    inside_circle = 0
    for i in range(0,attempts):
        x = random.uniform(0.0,1.0)
        y = random.uniform(0.0,1.0)
        point = x*x+y*y
        if point<=1:
            inside_circle += 1
    return(inside_circle/attempts*4)

def Leibniz_Formula(attempts):
    estimation = 0
    for k in range(attempts):
        divider = 1/(2*k+1)
        if k%2 == 0:
            estimation += divider
        else:
            estimation -= divider
    return 4*estimation

def Nilakantha_Series(attempts):
    estimation = 3
    for i in range(attempts):
        n = (i+1)*2
        estimation += 4*(-1)**i/n/(n+1)/(n+2)
    return (estimation)
# Run estimator 1,000,000 times to get more precise result
print(MC_PI_calculator(1000000))
print(Leibniz_Formula(1000000))
print(Nilakantha_Series(1000))
