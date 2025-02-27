from turtle import *
import turtle
from time import sleep
t = turtle.Turtle()

speed(10)

pensize(1)
color("black")

# Left side positions
penup()
goto(-10, 0)
pendown()

# Left side of the logo
lt(90)
fd(70)
lt(50)
fd(300)
lt(140)
fd(330)
lt(80)
fd(50)
lt(27)
fd(140)
end_fill()

# Inside of left part
penup()
goto(-10, 35)
pendown()

lt(118)
fd(229)
lt(129)
fd(230)
lt(86)
fd(45)
lt(38)
fd(159)
penup()
lt(106.5)
fd(229)
pendown()
rt(31)
fd(105)

# Right side positions
penup()
goto(10, 0)
pendown()

# Right side of the logo
rt(23.5)
fd(70)
rt(50)
fd(300)
rt(140)
fd(330)
rt(80)
fd(50)
rt(27)
fd(140)
# Inside of right part
penup()
goto(10, 35)
pendown()

rt(118)
fd(229)
rt(129)
fd(230)
rt(86)
fd(45)
rt(38)
fd(159)
penup()
rt(106.5)
fd(229)
pendown()
lt(31)
fd(105)

# Coloring of the right side upper part of the logo
color("black")
pensize(1)
penup()
goto(10, 35)
pendown()
begin_fill()
fillcolor("#655d57")
lt(24)
fd(35)
rt(50.5)
fd(300)
rt(154)
fd(106)
rt(30.8)
fd(230)
end_fill()

# Coloring of the left side upper part of the logo
color("black")
pensize(1)
penup()
goto(-10, 35)
pendown()
begin_fill()
fillcolor("#655d57")
rt(125.7)
fd(35)
lt(50.5)
fd(300)
lt(154)
fd(106)
lt(30.8)
fd(230)
end_fill()

# Coloring of the left side left part of the logo
color("black")
pensize(1)
backward(231)
begin_fill()
fillcolor("#9c938c")
rt(51)
fd(230)
rt(173.8)
fd(330)
rt(167)
fd(110)
end_fill()

# Coloring of the right side right part of the logo
color("black")
pensize(1)
penup()
goto(199, 167)
pendown()
begin_fill()
fillcolor("#9c938c")
rt(27)
fd(229.5)
lt(173.8)
fd(330)
lt(165)
fd(110)
end_fill()

# Coloring of the right side inner part of the logo
color("black")
pensize(1)
begin_fill()
fillcolor("#c7bfba")
rt(29.8)
fd(223.8)
lt(107)
fd(160)
lt(40)
fd(46)
lt(84.5)
fd(230)
end_fill()

# Coloring of the left side inner part of the logo
color("black")
pensize(1)
penup()
goto(-194.2, 164)
pendown()
begin_fill()
fillcolor("#c7bfba")
rt(121)
fd(223.8)
rt(107)
fd(160)
rt(40)
fd(46)
rt(84.5)
fd(230)
end_fill()

# Coloring of the left side bottom part of the logo
color("black")
penup()
goto(-10, 35)
pendown()
begin_fill()
fillcolor("#9c938c")
lt(123.8)
fd(160)
lt(168.5)
fd(142)
lt(65)
fd(35)
end_fill()

# Coloring of the right side bottom part of the logo
color("black")
penup()
goto(10, 35)
pendown()
begin_fill()
fillcolor("#9c938c")
rt(129.5)
fd(160)
rt(168.5)
fd(142)
rt(65)
fd(35)
end_fill()

penup()
goto(136, -64)
pendown()
pensize(2)
rt(88)
fd(48)

# Name of the design
color('silver')
penup()
goto(-120, -120)
pendown()
x = ('cambria', 35, 'bold')
# x = ('Georgia', 35, 'bold')
# x = ('Lucida', 34, 'italic', 'bold')
write('MAHINDRA', font=x)

# Name of the coder
color('#F4ADFF')
penup()
goto(140, -240)
pendown()
x = ('Lucida', 24, 'italic')
write('-Preetham', font=x)

# hideturtle()
# t.hideturtle()
isvisible()
turtle.done()
