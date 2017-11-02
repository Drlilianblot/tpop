'''
Created on 24 Jul 2014

@author: Lilian
'''

import turtle
my_turtle = turtle.Turtle()
my_turtle.showturtle()

# square size
length = 2
increase = 0.1


for i in xrange(360):
    my_turtle.forward(length)
    my_turtle.right(10)
    length = increase+length
    







## Must be the last line of code 
my_turtle.screen.exitonclick()
