import turtle
import random

colors = ["green", "red", "blue", "yellow", "purple", "pink"]

def load_window():
    window = turtle.Screen()
    window.bgcolor("black")

def draw_rhombus(some_turtle):
# draw 3 rhombus at a time
    for i in range(1,4):
        some_turtle.forward(75)
        some_turtle.right(60)
        some_turtle.forward(100)
        some_turtle.right(120)
        some_turtle.forward(100)
        some_turtle.right(60)
        some_turtle.forward(75)

def draw_hexagon(some_turtle):
  # executing loop 6 times for 6 sides
  for i in range(6):
    # Move forward by 90 units
    some_turtle.forward(90)
    # Turn left the turtle by 300 degrees
    some_turtle.left(300)

def sketch_a_flower ():
    bug = turtle.Turtle()
    bug.speed(30)
    bug.shape("turtle")
    
    for i in range(1,37):
     bug.color(colors[random.randint(0, 5)])
     draw_hexagon(bug)
     draw_rhombus(bug)
     bug.right(50)
    bug.right(90)
    bug.forward(300)
load_window()
sketch_a_flower()

def exit_window():
    window = turtle.Screen()
    window.exitonclick()
exit_window()