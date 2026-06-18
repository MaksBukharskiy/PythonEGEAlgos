from turtle import *

screensize(2000, 2000)
tracer(0)
lt(90)
k = 10

for i in range(2):
    forward(28*k)
    rt(90)
    forward(18*k)
    rt(90)

up()

forward(14 * k)
rt(90)
forward(10 * k)
lt(90)

down()

for i in range(2):
    forward(30*k)
    rt(90)
    forward(7*k)
    rt(90)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(3, 'red')

done()

