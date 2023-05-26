from turtle import *
from math import *

width(8)
hideturtle()

def polygoneXY(rayon,nombrecote):
    angle=2*pi/nombrecote
    up()
    goto(rayon,0)
    down()
    for i in range(nombrecote+1):
        goto(rayon*cos(angle*i),rayon*sin(angle*i))

for i in range(3,7):
    polygoneXY(30*i,i)
done()
