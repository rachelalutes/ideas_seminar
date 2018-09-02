import turtle
import random
flower = turtle.Pen()
flower.speed(0)

def circles(radius, radius2, rotation):
    flower.circle(radius,180)
    flower.begin_fill()
    flower.circle(radius2)
    flower.end_fill()
    flower.right(rotation)

num = random.randint(3,15)
num2 = num
for i in range(num):
    num2 -= 1
    flower.left(5)
    flower.color((random.random(),random.random(),random.random()))
    if num2 == 2: break
    for j in range(num2): circles(60,50,(180-(360/num2)))

flower.color("yellow")
flower.penup()
flower.goto(0,30)
flower.left(45)
flower.pendown()
flower.begin_fill()
flower.circle(50)
flower.end_fill()

turtle.done()