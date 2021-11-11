from myTurtle import *
import turtle

inStr = ''
swidth, sheight = 300, 300
tx, ty, t_angel, t_size = [0]*4

turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth+50, hegiht=sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(10)

inStr = getString()

for ch in inStr:
    tx, ty, t_angel, t_size = getXYAS(swidth, sheight)
    r, g, b = getRGB()

    turtle.goto(tx, ty)
    turtle.left(t_angel)

    turtle.color(r, g, b)
    turtle.white(ch, front=('맑은 고딕', t_size, 'bold'))

turtle.done