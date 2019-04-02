# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 12:59:17 2018

@author: lucasad
"""

import numpy as np

flottant = np.float32
a = 1.0
i = int(input())


for b in range(1, i):
    print(b, flottant(1.0) + flottant(float("1e-" + str(b))))
