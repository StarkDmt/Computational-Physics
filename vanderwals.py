# -*- coding: utf-8 -*-
import numpy as np

import matplotlib.pyplot as plt
from collections import namedtuple
from scipy import optimize
from scipy import integrate

def matrix (a0, a1, a2):
    matr = [[0, 0, -a0], [1, 0, -a1], [0,1, -a2]]
    matr = np.asarray(matr)
    return matr

def roots (matrix):
    e, v = np.linalg.eig(matrix)
    return e

def integral_diff(f, a, b, p):
    return (integrate.quad(f, a, b)[0] - p * (b - a))
    
def dichotomy(tau = 0.9, rtol = 1e-5):
    p_right = 0.6
    p_left = 0.1
    p_0 = 0.35
    a_0 = -1/p_0
    a_1 = 3/p_0
    a_2 = -(p_0 + 8 * tau)/(3 * p_0)
    root = roots(matrix(a_0, a_1, a_2))
   
    a = np.min(root)
    b = np.max(root)
    last = integral_diff(pii, a, b, p_0)
    new = 100000
    
    
    while ((np.abs ((new - last) / new)) > rtol):
        if (new > 0):
            p_0 = (p_right + p_0) / 2
            p_left = p_0
        else:
            p_0 = p_0 = (p_0 + p_left) / 2
            p_right = p_0
        last = new
        a_0 = -1/p_0
        a_1 = 3/p_0
        a_2 = -(p_0 + 8 * tau)/(3 * p_0)
        root = roots(matrix(a_0, a_1, a_2))
        print(root)
        a = np.min(root)
        b = np.max(root)
        new = integral_diff(pii, a, b, p_0)
        print(p_0)
    return p_0
        
    
def pii(fi, tau=0.9):
    """vdW pressure given volume& temperture. Reduced units."""
    return (8*tau*fi**2/3. - 3*fi + 1) / (fi**3 - (fi**2)/3. )


x = np.linspace(0.5, 3, 1000)
y = pii(x, 0.9)
y1 = np.zeros(1000)
res = dichotomy(0.9, 1e-5)
y1 += res


plt.plot(x,y)
plt.plot(x, y1)

plt.show()
    
    



    
    
