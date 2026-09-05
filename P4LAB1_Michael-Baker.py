# Michael Baker
# 9/5/26
# P4Lab1 
# This will draw a square and triangle with Turtle graphics
#imports the tools needed to use Turtles
import turtle
# Specifies the window, the color of the BG, and creates the two Turtles I used
win = turtle.Screen()
win.bgcolor("pink")
t = turtle.Turtle()
p = turtle.Turtle()
#Set specifications for the Turtles that affect how they draw and what they look like
p.pensize(3)
p.pencolor("green")
p.shape("turtle")
t.pensize(3)
t.pencolor("blue")
t.shape("turtle")

#Sets the fill color of the triangle to blue
t.fillcolor("blue")
#Runs through the instructions to draw the triangle once, or as many times as specified in the range parentheses. 

for i in range(1):
    t.begin_fill()
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)


    t.end_fill()


#Sets the fill color for the square to green
p.fillcolor("green")
#uses the while loop, but uses it basically like a for loop because I put the command to stop the program at the end of the loop. Would technically just keep going if I didn't.
while i in range(1):
    p.begin_fill()
    p.forward(100)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(100)

    p.end_fill()
    win.mainloop()
