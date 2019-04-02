# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:21:36 2018

@author: lucasad
"""

R1 = 2
R2 = 4.2
R3 = 10
V = 12

R_total = R1 + (1/((1/R2)+(1/R3)))
I_total = V/R_total
V1 = R1*I_total
V2 = V-V1
I2 = V2/R2

print(I2)