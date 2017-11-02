'''
Created on 23 Nov 2015

@author: lilia
'''
from shapes2D import Point2D

if __name__ == '__main__':
    p1 = Point2D()
    p2 = Point2D(2,2)
    print(p1, p2)
    print(p1.translate(1,3), p1)
    p1 = p1.translate(1,3)
    shape = [Point2D(1,1), Point2D(), Point2D(1,3)]
    print(p1, p1 != Point2D(0,3), p1 in shape)  
    print(p1 + p2)
    print(p1)  
    print((p1 + p2) * 3)