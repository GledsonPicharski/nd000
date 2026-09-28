import turtle

# Write a function here that creates a
# turtle and draws a shape with it.
def draw_triangle(color, start_point):
    jack = turtle.Turtle()
    jack.speed(0)
    jack.width(5)
    jack.color(color)
    jack.right(start_point)
    for start_point in range(6):
        for i in range(3):
            jack.forward(100)
            jack.right(120)
        jack.right(15)


# Call the function multiple times.
for color, start_point in zip(["red","orange", "blue"],[0,120,240]):
    draw_triangle(color,start_point)

turtle.done()