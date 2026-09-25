import turtle

amy = turtle.Turtle()
amy.color("green")

for side in [1, 2, 3, 4]:
    amy.forward(100)
    amy.right(90)

turtle.done()  # mantém a janela aberta