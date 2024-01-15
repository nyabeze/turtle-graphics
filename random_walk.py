
import turtle
import random


tim = turtle.Turtle()
turtle.colormode(255)


direction = [0, 90, 180, 270]
tim.width(5)
tim.shape("circle")
tim.shapesize(0.35)
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


for _ in range(500):
    tim.color(random_color())
    tim.right(random.choice(direction))
    tim.forward(10)

