import turtle
import random
t=turtle.Turtle()
s=turtle.getscreen()
t.speed(0)



for I in range(100):
    x=random.randint(-220,220)
    y=random.randint(-540,540)
    t.penup()
    t.goto(x,y)
    colors=['red','blue','green','black','orange','purple','yellow']
    t.color(colors[I%7])
    t.begin_fill()
    for I in range(5):
        t.down()
        t.fd(60)
        t.lt(144)
    t.end_fill()
t.up()
t.goto(-240,100)
t.down()
t.color('black')
t.begin_fill()
t.circle(100)
t.end_fill()
t.goto(-210,100)
t.color('white')
t.begin_fill()
t.circle(100)
t.end_fill()






    
    


    
