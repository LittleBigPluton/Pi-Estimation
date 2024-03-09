###############################
#####   Import libraries  #####
###############################

import math
import random

###############################
#####  PI From MC Method  #####
###############################

def MC_PI_calculator (attempts):
    # Create counter how many data point inside quarter circle
    inside_circle = 0
    # Generate data points
    for i in range(0,attempts):
        x = random.uniform(0.0,1.0)
        y = random.uniform(0.0,1.0)
    # Calculate point's coordinate
        point = x*x+y*y
    # Check if the point is in the circle area or not
        if point<=1:
            inside_circle += 1
    # Calculate ratio of data point inside
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

def Gauss_Legendre(attempts):
    #Initialize values
    a, b, t, p = 1, 1/math.sqrt(2), 1/4, 1
    #Define Arithmetic Geometric Means
    a_next = lambda a,b: (a+b)/2
    b_next = lambda a,b: math.sqrt(a*b)
    t_next = lambda a,a_next,p,t: t-p*(a-a_next)**2
    #Calculate variables at the desired iteration
    for _ in range(attempts):
        a_n1 = a_next(a,b)
        b = b_next(a,b)
        t = t_next(a,a_n1,p,t)
        p = p*2
        a = a_n1
    #Return estimation
    return ((a+b)**2)/4/t
