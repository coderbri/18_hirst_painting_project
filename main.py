import random
import turtle as turtle_module
from color_extraction import color_list

turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Starting turtle from the lower left corner
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Draw the Spot Painting
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        """If dot count is a tens (i.e., 40, 50, 60,... etc.), create a new line."""
        tim.setheading(90)      # turn left (face north)
        tim.forward(50)         # move forwards north
        tim.setheading(180)     # turn left again (face west)
        tim.forward(500)        # move forwards west, above 1st dot
        tim.setheading(0)       # go back to facing east


screen = turtle_module.Screen()
screen.exitonclick()
