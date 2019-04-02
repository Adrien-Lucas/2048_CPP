# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 12:54:45 2018

@author: lucasad
"""

from turtle import *

reset()
#hideturtle ()
speed(0)
delay(0)

def trace_carre (longueur):
    for i in range(4):
        forward(longueur)
        right(90)
        
def trace_polygone (longueur, cote):
    for i in range(cote):
        forward(longueur / cote)
        right(360 / cote)
        
def trace_etoile():
    for i in range(6):    
        forward(100)
        right(120)
        forward(100)
        left(60)
        
def koch_1(n, longueur):
    if n == 0:
        forward(longueur)
    if n == 1:
        forward(longueur/3)
        left(60)
        forward(longueur/3)
        right(120)
        forward(longueur/3)
        left(60)
        forward(longueur/3)
    if n >= 2:
        koch_1(n-1, longueur/3)
        left(60)
        koch_1(n-1, longueur/3)
        right(120)
        koch_1(n-1, longueur/3)
        left(60)
        koch_1(n-1, longueur/3)

angle = 30
left(90)
def  arbre(n, longueur ):
    if n == 0:
        color("red")
        forward(longueur)
        backward(longueur)
        color("black")
    else:
        width(n)
        forward(longueur / 3)
        left(angle)
        arbre(n - 1, longueur / 3 * 2)
        right (2* angle)
        arbre(n - 1, longueur / 3 * 2)
        left(angle)
        backward(longueur / 3)
        
        
arbre(11, 500)
    
