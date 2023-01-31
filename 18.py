import turtle as t
import random

tim = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)



# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# for i in range(4):
#     timmy_the_turtle.right(90)
#     for j in range(10):
#         timmy_the_turtle.pd()
#         timmy_the_turtle.forward(10)
#         timmy_the_turtle.pu()
#         timmy_the_turtle.forward(10)





screen = t.Screen()
screen.exitonclick()

