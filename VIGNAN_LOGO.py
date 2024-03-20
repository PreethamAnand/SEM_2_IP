from turtle import *
import turtle
from time import sleep
t = turtle.Turtle()

pensize(1)
bgcolor("lightblue")
color("black")
penup()
goto(-200, 210)
pendown()
for j in range(4):
    fd(350)
    for i in range(9):
        rt(10)
        fd(10)
# Starting position of the star outline
penup()
end_fill()
goto(-139, 50)
rt(40)  # Sets the angle of the outline of the star
lt(3)
fd(100)
rt(92)
# First curve at the bottom left side
for i in range(5):
    lt(10)
    fd(8)
pendown()
fillcolor("#9900ff")
begin_fill()
rt(45)
lt(9)
fd(100)
lt(90)
fd(26)
lt(90)
fd(90)
rt(92)
# Second curve at the bottom right side
for i in range(4):
    lt(10)
    fd(8)
rt(70)
fd(90)
lt(90)
fd(26)
lt(90)
fd(90)
rt(92)
lt(10)
# Third curve at the top right side
for i in range(5):
    lt(10)
    fd(8)
rt(70)
fd(90)
lt(90)
fd(26)
lt(90)
fd(90)
rt(92)
lt(10)
# Fourth curve at the top side
for i in range(4):
    lt(10)
    fd(8)
rt(70)
fd(90)
lt(90)
fd(26)
lt(90)
fd(90)
# F
rt(92)
lt(10)
# Fifth curve at the top side
for i in range(5):
    lt(10)
    fd(8)
rt(70)
fd(90)
lt(90)
fd(26)
lt(90)
fd(90)
rt(92)
lt(10)
for i in range(5):
    lt(10)
    fd(6)
rt(2)
fd(1)
fd(2)
end_fill()
# Outline of inside outer circle
penup()
lt(2)
lt(25)
fd(22)
pendown()
fillcolor('white')
begin_fill()
circle(40)
end_fill()


hideturtle()
t.hideturtle()
turtle.done()


''' lt(90)
fd(30)
lt(90)
fd(110)
lt(90) '''


''' # Top semi-circle
# penup()
# goto(-139, 90)
# lt(3)
# pendown()
# fillcolor("#9900ff")
# begin_fill()
# pencolor("#9900ff")
# lt(75)
# fd(90)
# lt(107)
# fd(10)
# for i in range(3):
#     lt(10)
#     fd(20)
#     lt(10)
#     fd(25)
# lt(10)
# fd(10)
# end_fill()'''
