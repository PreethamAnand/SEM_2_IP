from turtle import *
import turtle
from time import sleep
t = turtle.Turtle()


pensize(1)
color("black")
penup()
goto(-150, 0)
pendown()
fillcolor("black")
begin_fill()
# Outer logo box
lt(90)
fd(100)
# Top line
for i in range(5):
    rt(15)
    fd(10)
rt(15)
fd(280)
# Right line
for i in range(5):
    rt(15)
    fd(10)
rt(15)
fd(280)
# Bottom line
for i in range(5):
    rt(15)
    fd(10)
rt(15)
fd(280)
# Left line
for i in range(5):
    rt(15)
    fd(10)
rt(15)
fd(280)
end_fill()

# N positions
penup()
goto(-60, -130)
pendown()
# N color
pensize(1)
# First line of n
color("#C71F27")
begin_fill()
# fillcolor("#E50914")
fillcolor("#C71F27")
fd(200)
rt(90)
fd(35)
rt(90)
fd(200)
rt(90)
fd(35)
end_fill()

# Second line position of N
penup()
goto(40, -130)
pendown()
# Second line of N
color("#C71F27")
begin_fill()
fillcolor("#C71F27")
rt(90)
fd(200)
rt(90)
fd(35)
rt(90)
fd(200)
end_fill()

# Middle line of N
color("red")
begin_fill()
fillcolor("red")
rt(153.7)
fd(224)
lt(64)
fd(36.5)
lt(116.5)
fd(224.4)
lt(63)
fd(36.5)
end_fill()

# Name of the coder
color('white')
penup()
goto(60, -200)
pendown()
x = ('Lucida', 15, 'italic')
write('-Preetham', font=x)


hideturtle()
t.hideturtle()
turtle.done()
