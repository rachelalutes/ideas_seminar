import turtle
flower = turtle.Pen()
flower.speed(0)
flower.color("red")
flower.fillcolor("red")
flower.begin_fill()
for i in range(7):
    flower.circle(60,180)
    flower.begin_fill()
    flower.circle(50)
    flower.end_fill()
    flower.right(128.571429)
flower.color("orange")
flower.fillcolor("orange")
flower.left(5)
for i in range(6):
    flower.circle(60,180)
    flower.begin_fill()
    flower.circle(50)
    flower.end_fill()
    flower.right(120)
flower.color("yellow")
flower.fillcolor("yellow")
flower.left(5)
for i in range(5):
    flower.circle(60,180)
    flower.begin_fill()
    flower.circle(50)
    flower.end_fill()
    flower.right(108)
flower.color("green")
flower.fillcolor("green")
flower.left(5)
for i in range(4):
    flower.circle(60,180)
    flower.begin_fill()
    flower.circle(50)
    flower.end_fill()
    flower.right(90)
flower.color("blue")
flower.fillcolor("blue")
flower.left(5)
for i in range(3):
    flower.circle(60,180)
    flower.begin_fill()
    flower.circle(50)
    flower.end_fill()
    flower.right(60)
flower.color("purple")
flower.fillcolor("purple")
flower.left(3)
for i in range(3):
    flower.circle(50,180)
    flower.begin_fill()
    flower.circle(40)
    flower.end_fill()
    flower.right(60)
turtle.done()
