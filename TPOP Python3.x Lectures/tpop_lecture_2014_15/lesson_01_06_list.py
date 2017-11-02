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
         

def draw_multicolour_squares(number, max_size, decrease, list_colours):  
    length = max_size  
    for n in xrange(number):
        pos_in_list = n%len(list_colours)
        fill_square(-length/2, length/2, length, list_colours[pos_in_list])
        length = length - decrease


draw_multicolour_squares(20, 200, 10, ['red','yellow', 'orange', 'green', 'cyan', 'blue', 'white'])
## Must be the last line of code 
my_turtle.screen.exitonclick()
