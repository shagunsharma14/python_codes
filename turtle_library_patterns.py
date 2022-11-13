import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("purple2")

# -----------------------------------------------------------------------------------------------------------------------
# TODO: Shape generator (3-10 sided figure)
# NOOB'S WAY
# ----------------------------------------------------------
# tim.goto(-100, 250)
#
#
# def draw_line():
#     # for i in range(10):
#     #     tim.forward(10)
#     #     tim.pendown()
#     #     tim.forward(10)
#     #     tim.penup()
#     tim.pendown()
#     tim.forward(100)
#
#
# def square():
#     draw_line()
#     tim.right(90)
#     draw_line()
#     tim.right(90)
#     draw_line()
#     tim.right(90)
#     draw_line()
#
#
# def trianle():
#     tim.color("green")
#     for i in range(3):
#         draw_line()
#         tim.right(120)
#
#
# def pentagon():
#     tim.color("red")
#     tim.right(90)
#     for i in range(5):
#         draw_line()
#         tim.right(72)
#
# def hexagon():
#     tim.color("DarkCyan")
#     for i in range(6):
#         draw_line()
#         tim.right(60)
#
# def heptagon():
#     tim.color("gold4")
#     for i in range(7):
#         draw_line()
#         tim.right(51.42)
#
# def octagon():
#     tim.color("LemonChiffon4")
#     for i in range(8):
#         draw_line()
#         tim.right(45)
#
# def nonagon():
#     tim.color("maroon4")
#     for i in range(9):
#         draw_line()
#         tim.right(40)
#
# def decagon():
#     tim.color("salmon")
#     for i in range(10):
#         draw_line()
#         tim.right(36)
#
#
# trianle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# # decagon()
# PRO WAY
# ------------------------------------------------------------------------------------------------------------------------
# import random
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#           "SeaGreen"]
# def shape(no_sides):
#     angle = 360/no_sides
#     for _ in range(no_sides):
#         tim.forward(100)
#         tim.right(angle)
# tim.pendown()
# for shape_side_n in range(3,10):
#         tim.color(random.choice(colours))
#         shape(shape_side_n)

# --------------------------------------------------------------------------------------------
# todo: Random Walk Generator
# 1 random walk same distance
# 2 everystep different color
# 3 Thickness of the drawing scene
# 4 speed up the turtle
# import random
#
# for j in range(1000):
#     tim.color(random.random(), random.random(), random.random())
#     # tim.fillcolor(random.random(),random.random(),random.random())
#     tim.pendown()
#     tim.pensize(5)
#     tim.speed(0)
#     tim.setheading(random.randrange(0, 360, 90))
#     tim.forward(25)

# --------------------------------------------------------------------------------------------
# TODO: SPIROGRAPH
# random color
# how to draw a circle
# how large a circle can be
# repeatedly draw a circle
# change the tilt of a circle little by little
# tim.speed(0)
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random.random(), random.random(), random.random())
#         tim.circle(100)
#         tim.setheading(tim.heading()+size_of_gap)
#
# draw_spirograph(5)




screen = Screen()
screen.exitonclick()
