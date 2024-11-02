# Tutorial for using turtle graphics in Python

# Import the turtle module
import turtle

# Create the turtle window
window = turtle.Screen()

# Set the title of the window
window.title("My First Turtle Graphics")

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for i in range(4):
    t.forward(100)
    t.right(90)

# Run the turtle graphics
turtle.done()


