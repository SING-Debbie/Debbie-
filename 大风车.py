from turtle import *
speed(100)
bgcolor("black")
colors = ["red","yellow","blue","orange","green","purple"]

for i in range(300):
    width(i*6//300)
    pencolor(colors[i%6])
    forward(i)
    left(61)



done()


   
