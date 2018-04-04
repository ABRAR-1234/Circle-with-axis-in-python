
# coding: utf-8

# In[1]:


import turtle
myT=turtle.Turtle()
# draw your circle 
myT.circle(200)
# rotate so you are looking towards the centre of the circle
myT.left(90)
# lift the pen so no line is drawn
myT.penup()
myT.forward(180)
# put pen down now (if you need to)
myT.pendown()
# rotate back (if you need to)
myT.right(90)
def draw_axis(s):
    # draws x, y axis
    myT.color("black")
    myT.pensize(2)
    for i in range(4):
        myT.fd(s)
        myT.pu()
        myT.goto(0,180)
        myT.pd()
        myT.lt(90)
        myT.ht()    
    exitonclick()
draw_axis(200)
myT.right(90)
myt.fd(s)

