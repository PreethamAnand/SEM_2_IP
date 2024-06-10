# from turtle import *
# import turtle
# from time import sleep

# t = turtle.Turtle()

# pensize(1)
# bgcolor("lightblue")
# color("black")
# penup()
# goto(-200, 210)
# pendown()
# for j in range(4):
#     fd(350)
#     for i in range(9):
#         rt(10)
#         fd(10)

# # Starting position of the star outline
# penup()
# end_fill()
# goto(-139, 50)
# rt(40)  # Sets the angle of the outline of the star
# lt(3)
# fd(100)
# rt(92)

# # First curve at the bottom left side
# for i in range(5):
#     lt(10)
#     fd(8)
# pendown()
# fillcolor("#9900ff")  # Violet color
# begin_fill()
# rt(45)
# lt(9)
# fd(100)
# lt(90)
# fd(26)
# lt(90)
# fd(90)
# rt(92)

# # Second curve at the bottom right side
# for i in range(4):
#     lt(10)
#     fd(8)
# rt(70)
# fd(90)
# lt(90)
# fd(26)
# lt(90)
# fd(90)
# rt(92)
# lt(10)

# # Third curve at the top right side
# for i in range(5):
#     lt(10)
#     fd(8)
# rt(70)
# fd(90)
# lt(90)
# fd(26)
# lt(90)
# fd(90)
# rt(92)
# lt(10)

# # Fourth curve at the top side
# for i in range(4):
#     lt(10)
#     fd(8)
# rt(70)
# fd(90)
# lt(90)
# fd(26)
# lt(90)
# fd(90)
# rt(92)
# lt(10)

# # Fifth curve at the top side
# for i in range(5):
#     lt(10)
#     fd(8)
# rt(70)
# fd(90)
# lt(90)
# fd(26)
# lt(90)
# fd(90)
# rt(92)
# lt(10)
# for i in range(5):
#     lt(10)
#     fd(6)
# rt(2)
# fd(1)
# fd(2)
# end_fill()

# # Outline of inside outer circle
# penup()
# lt(2)
# lt(25)
# fd(22)
# pendown()
# fillcolor("white")  # White color for inner circle
# begin_fill()
# circle(40)
# end_fill()

# penup()
# circle(10, 20)  # Move turtle to starting position of the star
# pendown()
# lt(90)

# # CODE FOR CREATING THE STAR
# color("yellow")  # Yellow color for the star
# for i in range(5):
#     fd(75)
#     rt(144)

# hideturtle()
# t.hideturtle()
# turtle.done()
import turtle

# Create a screen
screen = turtle.Screen()
screen.setup(width=500, height=400)
screen.title("Vignan Institute of Engineering for Women Logo")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the speed of the turtle

# Set background color as blue
t.penup()
t.goto(-250, -200)
t.pendown()
t.fillcolor("lightblue")
t.begin_fill()
t.circle(200)
t.end_fill()

# Set the outline color as purple
t.penup()
t.goto(-250, -200)
t.pendown()
t.color("purple")
t.circle(200)

# Move the turtle to draw the star
t.penup()
t.goto(-50, 0)
t.pendown()
t.left(90)
t.fillcolor("yellow")
t.begin_fill()

# Draw the star using a for loop
for _ in range(5):
    t.forward(100)
    t.right(144)

t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until closed manually
screen.mainloop()
