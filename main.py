# import colorgram
# rgb_colors =[]
# colors = colorgram.extract('imagecolor.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     my_tuples = (r, g, b)
#     rgb_colors.append(my_tuples)
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
from image_color import image_colorlist
import random
turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
screen = Screen()

tim.speed(0)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101
for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(image_colorlist))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)














screen.exitonclick()