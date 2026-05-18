from turtle import *

tracer(0)
screensize(2000, 2000)

lt(90)
k = 20

rt(90)
for i in range(7):
    rt(45)
    fd(11*k)
    rt(45)
    
up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(3, "red")

done()