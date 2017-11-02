'''
Created on 24 Jul 2014

@author: Lilian
'''

import turtle
my_turtle = turtle.Turtle()
my_turtle.showturtle()

# square size
length = 10
increase = 10

def draw_square(start_x, start_y, size):
    my_turtle.penup()
    my_turtle.goto(start_x,start_y)
    my_turtle.pendown()
     
    for i in xrange(4):
        my_turtle.forward(size)
        my_turtle.right(90)
    
    my_turtle.penup()
         

# draw_square(0,0,30)
# draw_square(0,0,length)

for n in xrange(20):
    
    draw_square(-length/2, length/2, length)
    
    length = length + increase
    

## Must be the last line of code 
my_turtle.screen.exitonclick()
