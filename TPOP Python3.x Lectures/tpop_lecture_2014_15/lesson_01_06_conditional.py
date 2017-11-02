'''
Created on 24 Jul 2014

@author: Lilian
'''

import turtle
my_turtle = turtle.Turtle()
my_turtle.showturtle()

# square size
length = 210
increase = 10

def fill_square(pos_x, pos_y, size, fill_colour):
    my_turtle.penup()
    my_turtle.goto(pos_x,pos_y)
    my_turtle.pendown()
    
    my_turtle.fill(True)
    my_turtle.fillcolor(fill_colour)
     
    for i in xrange(4):
        my_turtle.forward(size)
        my_turtle.right(90)
    
    my_turtle.fill(False)
    my_turtle.penup()
         

# draw_square(0,0,30)
# draw_square(0,0,length)

# for n in xrange(20):
#     if n%2 == 0:
#         fill_square(-length/2, length/2, length, "red")
#         
#     else:
#         fill_square(-length/2, length/2, length, "blue")
#     
#     length = length - increase


    
for n in xrange(20):
    if n%3 == 0:
        fill_square(-length/2, length/2, length, "red")
    
    elif n%3 == 1:
        fill_square(-length/2, length/2, length, "yellow")        
    
        
    else:
        fill_square(-length/2, length/2, length, "cyan")
    
    length = length - increase

## Must be the last line of code 
my_turtle.screen.exitonclick()
