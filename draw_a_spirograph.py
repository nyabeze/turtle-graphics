import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)

tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(120)
        tim.right(size_of_gap)


draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()