#making sierpinski triangle with turtle and for lops

import turtle as trutle
import time

screen = trutle.Screen()

screen.tracer(0) 

length = 400
#variable that that can be galfed


#setup
e = trutle.Turtle()
e.width(1)
e.speed(0)
e.hideturtle()
e.setpos(0,0)

#infinite triangles that are half length of previous ones and half positions so it makes sierpinski triangle
def triangle(length):
    for i in range(3):
        e.forward(length)
        e.right(120) #turns 120 degrees to form 60 degree interior engle

def s_triangle(length, length2):
    if length2 == 0:
        triangle(length)
    else:
        s_triangle(length/2, length2-1) 
        e.forward(length/2) #move the psotition for new triangle
        s_triangle(length/2, length2-1)
        e.backward(length/2)
        e.right(60)#top most riangle
        e.forward(length/2)
        e.left(60)
        s_triangle(length/2, length2-1)
        e.right(60)#resets
        e.backward(length/2)
        e.left(60)

s_triangle(length, 6)


screen.update()


screen.exitonclick()
#easy way toi exit