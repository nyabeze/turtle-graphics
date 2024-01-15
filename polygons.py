from turtle import Turtle

tim = Turtle()
tim.color("cyan")

number_of_sides = 3


def draw_polygon(sides):
    angle = 360/sides
    for side in range(sides):
        tim.forward(100)
        tim.right(angle)


while number_of_sides < 11:
    draw_polygon(number_of_sides)
    number_of_sides += 1
