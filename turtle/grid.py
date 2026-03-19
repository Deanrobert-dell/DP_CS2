import turtle

def draw_axes(t):
    """Draws the X (Time) and Y (Net Income) axes starting from 0,0."""
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(300, 0)  
    t.write(" Time Passed", align="left")
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(0, 300)  
    t.write(" Net Income", align="left")
    t.penup()

def plot_net_income(t, data):
    """Plots net income over time starting from (0,0)."""
    t.goto(0, 0)  
    t.color("green")
    t.pensize(3)
    t.pendown()
    
    
    for time, income in data:
        t.goto(time, income)
        t.dot(10, "black")


screen = turtle.Screen()
screen.title("Net Income Over Time")

screen.setworldcoordinates(-50, -50, 400, 400) 

chart_turtle = turtle.Turtle()
chart_turtle.speed(2)


financial_data = [(50, 10), (100, 15), (150, 12), (200, 25), (250, 30000)]


draw_axes(chart_turtle)
plot_net_income(chart_turtle, financial_data)

chart_turtle.hideturtle()
screen.exitonclick()
