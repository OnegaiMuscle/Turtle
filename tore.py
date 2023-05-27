from turtle import * 
width(4)
speed(0)
hideturtle()

def demipolygone(longueurcote,nombrecote,angle):
    for i in range(nombrecote):
        forward(longueurcote); left(angle)
    up()
    for i in range(nombrecote):
        forward(longueurcote); left(angle)
    down()

def Tore(x,n):
    N=2*n
    A1=180/n
    A2=180/N
    for i in range(N):
        demipolygone(x,N,A2)
        left(A2); forward(x); left(A2)
    for i in range(N):
        demipolygone(x,n,-A1)
        left(-A1)
        demipolygone(x,n,-A1)
        left(A2); backward(x); right(A2)

Tore(50,4)
done()
