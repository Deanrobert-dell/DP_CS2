import turtle as trutle

e = trutle.Turtle()

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