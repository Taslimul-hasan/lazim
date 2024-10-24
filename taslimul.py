import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(100)  # Fastest drawing speed

# Draw a colorful spiral
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(360):
    spiral_turtle.pencolor(colors[i % 6])  # Cycle through the colors
    spiral_turtle.width(i / 100 + 1)  # Increase the width gradually
    spiral_turtle.forward(i)  # Move forward
    spiral_turtle.left(59)  # Turn left

# Hide the turtle and finish
spiral_turtle.hideturtle()
turtle.done()
turtle.exitonclick()