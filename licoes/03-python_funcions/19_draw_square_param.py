import turtle
jack = turtle.Turtle()
jack.color("yellow")
    
def draw_square(length):
    for side in range(4):
        jack.forward(length)
        jack.right(90)

draw_square(100)
draw_square(50)
draw_square(25)