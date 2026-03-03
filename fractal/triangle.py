#making sierpinski triangle with turtle and for lops

import turtle as trutle
import time
from helpers import e, s_triangle

depth = int(input("choose depth 1-8: "))
color = input("choose color: ")
screen = trutle.Screen()

screen.tracer(1) 

length = 400
#variable that that can be galfed


#setup
e.width(1)
e.speed(0)
e.hideturtle()
e.setpos(0,0)
e.pencolor(color)
screen.bgcolor("black")

s_triangle(length, depth)

screen.update()

screen.exitonclick()
#easy way toi exit