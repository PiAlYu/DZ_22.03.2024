from turtle import *

screensize(1000, 1000)
tracer(1000)
n = 40
up()
for x in range(-50, 20):
    for y in range(-100, 120):
        goto(x * n, y * n)
        dot(3)
goto(-80, 80)
dot(10)
down()
x, y = -80, 80
color('red')
for i in range(10):
    x += 4 * n
    y += 3 * n
    goto(x, y)
    x -= 4 * n
    y += 10 * n
    goto(x, y)
    x += 18 * n
    y -= 12 * n
    goto(x, y)
    x -= 24 * n
    y -= 12 * n
    goto(x, y)
    dot(10)
done()
