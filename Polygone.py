from turtle import *

hideturtle()
width(8)

def triangle(longueurcote):
    angle=120
    for i in range(3):
        forward(longueurcote); right(angle)

def carre(longueurcote):
    angle=90
    for i in range(4):
        forward(longueurcote); right(angle)

def pentagone(longueurcote):
    angle=72
    for i in range(5):
        forward(longueurcote); right(angle)

def hexagone(longueurcote):
    angle=60
    for i in range(6):
        forward(longueurcote); right(angle)

def octogone(longueurcote):
    angle=45
    for i in range(8):
        forward(longueurcote); right(angle)

def polygone(longueurcote,nombrecote):
    angle=360/nombrecote
    for i in range(nombrecote):
        fd(longueurcote); right(angle)

polygone(60,3)
polygone(80,4)
polygone(100,5)
polygone(120,6)
done()
