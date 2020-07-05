from turtle import *
from random import *
from math import *
tracer(0)
def tree(w,l,min):
    pencolor("black")
    pd()
    r = randrange(6, 15)  # 对长度做随机
    w1 = w * 3 / 4  # 对宽度做递减
    if l >= 5:
        pensize(w1)
        s= random()*15+10
        fd(l)
        right(s)
        tree(w1,l-r,min)
        left(2*s)
        color()
        tree(w1,l-r,min)
        right(s)
        backward(l)
    elif l >= min:
        pensize(w1)
        s= random()*15+10
        fd(l)
        right(s)
        color()
        tree(w1,l-r,min)
        color()
        left(2*s)
        color()
        tree(w1,l-r,min)

        right(s)
        color()
        backward(l)
    else:
        color()


def mid(w,l,min):
    pencolor("black")
    r = randrange(6, 15)
    w1 = w * 3 / 4
    if l >= 5:      # 做中间的树枝
        pensize(w1)
        s = random() * 15 + 20
        fd(l)
        right(s)

        mid(w1, l - r, min)
        left(2 * s)
        color()
        mid(w1, l - r, min)
        right(s)
        backward(l)


    elif l >= min:
        pensize(w1)
        s= random()*15+20
        fd(0.7*l)
        right(s)
        color()
        mid(w1,l-r,min)
        color()
        left(2*s)
        color()
        right(s)
        color()
        left(s)
        mid(w1,l-r,min)
        right(s)
    else:
        color()
def color():
    right(90)
    x = (cos(heading() +30)) / 4 + 0.5
    pencolor(0.6*x, x * 0.6, x * 0.8)
    circle(3)

    left(90)

bgcolor("dimgrey")
left(180)
pu()
fd(100)
right(90)
backward(300)
pd()
tree(12,100,0)
fd(100)
mid(10,85,5)

ht()
update()
done()



