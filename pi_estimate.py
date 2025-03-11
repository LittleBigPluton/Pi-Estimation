###############################
#####   Import libraries  #####
###############################

import math
import random

########################################
#####  PI From Monte Carlo Method  #####
########################################

def MC_PI_calculator (attempts):
    # Create counter how many data point inside quarter circle
    inside_circle = 0
    # Generate data points
    for i in range(0,attempts):
        x = 1-random.uniform(0.0,2.0)
        y = 1-random.uniform(0.0,2.0)
    # Calculate point's distance from center of circle
        point = math.sqrt(x*x+y*y)
    # Check if the point is in the circle area or not
        if point<=1:
            inside_circle += 1
    # Calculate ratio of data point inside
    return(inside_circle/attempts*4)

#####################################
#####  PI From Leibniz Formula  #####
#####################################

def Leibniz_Formula(attempts):
    # Initialize estimation to zero
    estimation = 0
    # Iterate k values to simulate infinite sum up to some point
    for k in range(attempts):
        # Calculate division with respect to current iteration number
        division = 1/(2*k+1)
        # Decide sign of division
        if k%2 == 0:
            estimation += division
        else:
            estimation -= division
    return 4*estimation

#######################################
#####  PI From Nilakantha Series  #####
#######################################

def Nilakantha_Series(attempts):
    # Initialize estimation to 3 as start value
    estimation = 3
    # Iterate i values to simulate infinite sum up to some point
    for i in range(attempts):
        n = (i+1)*2
        estimation += 4*(-1)**i/n/(n+1)/(n+2)
    return (estimation)

####################################
#####  PI From Gauss Legendre  #####
####################################

def Gauss_Legendre(attempts):
    #Initialize values
    a, b, t, p = 1, 1/math.sqrt(2), 1/4, 1
    #Define next values of variables as inline function
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
