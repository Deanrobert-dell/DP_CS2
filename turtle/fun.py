import turtle as trutle
import time

screen = trutle.Screen()


e = trutle.Turtle()
e.width(3)
e.speed(0)
e.hideturtle()
e.setpos(0,0)
e.right(30)
e.forward(30)
e.left(25)
e.forward(80)
e.right(10)
e.forward(120)
e.left(30)
e.forward(20)
e.left(45)
e.forward(20)
e.left(30)
e.forward(5)
e.left(100)
e.forward(30)
e.right(35)
e.forward(130)
e.left(40)
e.forward(20)
e.right(60)
e.forward(40)
e.right(25)
e.forward(45)

e.left(90)
e.forward(30)
e.left(70)
e.forward(25)
e.right(60)
e.forward(25)

e.right(50)
e.forward(20)
e.left(60)
e.forward(5)
e.left(90)
e.forward(35)

e.setpos(0,0)
e.home()
e.penup()
e.setpos(250,-25)
e.pendown()
e.left(65)
e.forward(20)
e.left(30)
e.forward(15)
e.left(145)
e.forward(20)
e.right(30)
e.forward(20)

e.penup()
e.home()
e.setpos(225,-28)
e.left(70)
e.pendown()
e.forward(20)

e.left(30)
e.forward(15)
e.left(140)
e.forward(15)
e.right(25)
e.forward(10)
e.setpos(120,30)
e.setpos(113,22)

t = trutle.Turtle()
t.hideturtle()
t.width(3)
t.speed(0)
t.hideturtle()
t.left(60)
t.penup()
t.setpos(208, -22)
t.pendown()
t.forward(13)
t.penup()

t.penup()
t.setpos(190, -15)
t.pendown()
t.forward(13)
t.penup()

t.penup()
t.setpos(170, -6)
t.pendown()
t.forward(13)
t.penup()

t.penup()
t.setpos(150, 1)
t.pendown()
t.forward(13)
t.penup()

t.penup()
t.setpos(130, 12)
t.pendown()
t.forward(13)
t.penup()

t.setpos(218, -10)
t.pendown()
t.left(90)
t.forward(70)
t.left(90)
t.forward(10)


t.penup()
t.home()
t.setpos(30,100)
t.pendown()
t.right(15)
t.forward(60)
t.right(45)
t.forward(30)
t.left(70)
t.forward(70)
t.left(25)
t.forward(45)
t.right(50)
t.forward(50)
#hook end of top teeth
t.left(115)
t.forward(20)
t.right(25)
t.forward(30)
t.left(75)
t.forward(15)
t.left(10)
t.forward(30)
t.left(15)
t.forward(35)
t.right(20)
t.forward(35)
t.right(180)
t.forward(35)
t.left(145)
t.forward(35)
t.left(60)
t.forward(25)
#above eye
t.right(20)
t.forward(55)
t.left(25)
t.forward(65)
t.left(32)
t.forward(110)
t.left(40)
t.forward(45)

t.left(20)
t.forward(50)

t.left(90)
t.forward(20)

t.left(75)
t.forward(25)
t.setpos(30, 100)

t.penup()
t.home()
t.setpos(40, 175)
t.pendown()

t.left(25)
t.forward(30)

t.right(70)
t.forward(40)
t.right(70)
t.forward(20)

t.right(40)
t.forward(30)

t.right(40)
t.forward(20)

t.right(35)
t.forward(25)
t.setpos(40, 175)

t.penup()
t.home()

t.setpos(255, 85)
t.pendown()


t.right(80)
t.forward(25)

t.right(35)
t.forward(22)
t.right(150)
t.forward(20)
t.left(20)
t.forward(10)
t.setpos(255, 85)

t.penup()
t.home()
t.setpos(245, 70)
t.left(170)
t.pendown()
t.forward(20)

t.penup()
t.home()
t.setpos(210, 95)
t.pendown()

t.right(60)
t.forward(25)
t.right(40)
t.forward(32)

t.right(155)
t.forward(25)
t.left(35)
t.forward(12)

t.left(80)
t.forward(30)
t.right(28)
t.forward(70)
t.right(95)
t.forward(18)


t.penup()
t.home()
t.left(100)
t.setpos(130, 43)
t.pendown()
t.forward(18)

t.penup()
t.setpos(145, 48)
t.pendown()
t.forward(17)

t.penup()
t.setpos(160, 52)
t.pendown()
t.forward(17)

t.penup()
t.setpos(175, 56)
t.pendown()
t.forward(17)

t.penup()
t.setpos(190, 64)
t.pendown()
t.forward(15)

t.penup()
t.setpos(198, 72)
t.pendown()
t.left(30)
t.forward(15)

t.penup()
t.setpos(225, 75)
t.pendown()
t.right(35)
t.forward(18)

t.penup()
t.setpos(238, 73)
t.pendown()
t.right(20)
t.forward(17)

time.sleep(1)


t3= trutle.Turtle()
font_style = ("Times New Roman", 25, "normal")
t3.hideturtle()
t3.penup()
t3.goto(100,-150)
t3.pendown()
t3.write("You defeated Anubis, protector of the after life", font=font_style, align="center")

time.sleep(.5)

time.sleep(.5)

t3= trutle.Turtle()
font_style = ("Times New Roman", 25, "normal")
t3.hideturtle()
t3.penup()
t3.goto(100,-200)
t3.pendown()
t3.write("click to continue", font=font_style, align="center")

screen.exitonclick()






















