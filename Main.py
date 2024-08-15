#import colorgram
#
#rgb_colors = []
#colors = colorgram.extract('hirst.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#color_list = [ (215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56)]
#print(rgb_colors)

import turtle
import random

turtle.colormode(255)
color_list = [(215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213),
              (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18),
              (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167),
              (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197),
              (220, 177, 173), (14, 105, 56)]
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
