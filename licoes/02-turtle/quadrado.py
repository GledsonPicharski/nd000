import turtle

amy = turtle.Turtle()
amy.color("green") 
flag_four_colors = 0

#for side in [1, 2, 3, 4]:
for i in [0, 1, 2, 3]:
    if flag_four_colors:
        color = ["red","orange","yellow","green"]
        amy.color(color[i])
    amy.forward(100)
    amy.right(90)

turtle.done()  # mantém a janela aberta