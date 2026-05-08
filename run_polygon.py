from polygon import *
from turtle import Turtle

def main():
    t = Turtle()
    # Use a random color for visibility; the pencolor can be changed as needed
    t.pencolor("blue")
    t.hideturtle()

    # Draw a radial pattern of circles.  The radialPattern function expects
    # a callable that draws a shape given the turtle and a length parameter.  For
    # circles the length parameter is interpreted as a radius.  We choose 12
    # circles arranged around the origin to form a two‑dimensional graph.
    radialPattern(t, 12, 50, shape=circle)

    # Keep the window open until it is closed by the user
    t.getscreen().exitonclick()

if __name__ == "__main__":
    main()
