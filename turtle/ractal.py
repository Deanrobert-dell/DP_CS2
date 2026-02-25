# for loop program with input that asks use for shape and then turtle codes infinite random everytime pattern from shape
#infinite for loop turtle pattern
from turtle import *

def draw_shape(shape):
    if shape == "triangle":
        for i in range(3):
            forward(100)
            left(120)
    elif shape == "square":
        for i in range(4):
            forward(100)
            left(90)
    elif shape == "circle":
        circle(100)

while True:
    shape = input("Enter a shape (triangle, square, circle): ")
    draw_shape(shape)

