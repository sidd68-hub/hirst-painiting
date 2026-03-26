import colorgram
import turtle as t
import random

color = colorgram.extract('image.jpg',30)
colors_list = []

def get_rgb(rgb):
    r = rgb.rgb.r
    g = rgb.rgb.g
    b = rgb.rgb.b
    return (r,g,b)



for rgb in color:
    colors_list.append(get_rgb(rgb))

tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        
screen = t.Screen()
screen.exitonclick()