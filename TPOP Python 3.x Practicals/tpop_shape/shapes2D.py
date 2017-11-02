'''
Created on 23 Nov 2015

@author: lilia
'''

class Point2D(object):
    '''
    classdocs
    '''


    def __init__(self, x = 0, y = 0):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        
    def __str__(self):
        return "("+str(self._x) + ","+ str(self._y)+")"
    
    def __mul__(self, scalar):
        return self.scale(scalar)
        
    def __add__(self, point):
        if isinstance(point, Point2D):
            return self.translate(point.getX(), point.getY())
        else:
            raise TypeError('cannot add '+point.__class__()+ ' to a Point2D instance')
        
    def __eq__(self, point):
        if(isinstance(point, Point2D)):
            return point.getX() == self._x and point.getY() == self._y
        else:
            return False

    def __ne__(self, point):
        if(isinstance(point, Point2D)):
            return point.getX() != self._x or point.getY() != self._y
        else:
            return True

    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
    
    def get(self):
        return (self._x, self._y)
    
    def setX(self, x):
        self._x = x
        
    def setY(self, y):
        self._y = y
        
    def set(self, coord):
        if len(coord) == 2:
            self._x = coord[0]
            self._y = coord[1]
        else:
            raise ValueError("invalid parameter size")
        
#     def scale(self, scalar):
#         self._x *= scalar
#         self._y *= scalar
#         return self
        
    def scale(self, scalar):
        return Point2D(scalar * self._x, scalar * self._y)
         
#     def translate(self, x, y):
#         self._x *= x
#         self._y *= y
#         return self

    def translate(self, x, y):
        return Point2D(x + self._x, y + self._y)
        
        