#!/usr/bin/python3
import pi_estimate as PE
# Run MC estimator 1,000,000 times to get more precise result
print(PE.MC_PI_calculator(1000000))
# Run Leibniz Formula 100 times
print(PE.Leibniz_Formula(100))
# Run Nilakantha Series 100 times
print(PE.Nilakantha_Series(100))
# Run Gauss Legendre algorithm 10 times
print(PE.Gauss_Legendre(10))
