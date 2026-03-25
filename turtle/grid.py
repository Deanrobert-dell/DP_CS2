import turtle

def draw(t):
    
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(300, 0)  
    t.write("dates", align="left")
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(0, 300)  
    t.write(" net income", align="left")
    t.penup()

def plot(t, data):
    t.goto(0, 0)  
    t.color("green")
    t.pensize(3)
    t.pendown()
    
    
    for time, income in data:
        t.goto(time, income)
        t.dot(8, "black")


screen = turtle.Screen()
screen.title("net income")

screen.setworldcoordinates(-50, -50, 400, 400) 

chart_turtle = turtle.Turtle()
chart_turtle.speed(2)


financial_data = [(50, 10), (100, 15), (150, 12), (200, 25), (250, 30000)]


draw(chart_turtle)
plot(chart_turtle, financial_data)

chart_turtle.hideturtle()
screen.exitonclick()
