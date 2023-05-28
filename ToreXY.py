from turtle import * 
from math import *

setup(512,512)
bgcolor("red")
width(4)
speed(0)
hideturtle()

def Tore(R,n):
    A=2*pi/n
    B=A/2
    C=A/4
    
    def X(i,j):
        return R*cos(B*i-C+A*j)-R*cos(A*j+B)/(2*cos(C))
    def Y(i,j):
        return R*sin(B*i-C+A*j)-R*sin(A*j+B)/(2*cos(C))
    
    for j in range(0,n):
        up(); goto( X(1,j),Y(1,j) ); down()
        for i in range(2,n+4):
            goto( X(i,j),Y(i,j) )
    for j in range(0,n):
        for i in range(2,n):
            up(); goto( X(i,j),Y(i,j) ); down()
            goto( X(i+2,j-1),Y(i+2,j-1) )

Tore(160,8)
done()
