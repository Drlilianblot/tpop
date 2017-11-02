'''
Created on 23 Nov 2015

@author: lilian
'''

class Pair(object):
    '''
    classdocs
    '''
    _instances = 0

    def __init__(self, x = 0, y = 0):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        Pair._instances += 1
        
    def __str__(self):
        return "("+str(self._x) + ","+ str(self._y)+")"
    
    def __repr__(self):
        return "Pair('"+str(self._x) + "','"+ str(self._y)+"')"


    ## ACCESSORS
    
    def getFirst(self):
        return self._x
    
    def getSecond(self):
        return self._y

    ## MUTATORS
    
    def setFirst(self, x):
        self._x = x
        
    def setSecond(self, y):
        self._y = y
        












    ## OPERATORS    
    def multiplication(self, scalar):
        self._x *= scalar
        self._y *= scalar
        return self
        
    def add(self, pair):
        self._x *= pair.getFirst()
        self._y *= pair.getSecond()
        return self











##    def multiplication(self, scalar):
##        return Pair(scalar * self._x, scalar * self._y)
         


##    def add(self, pair):
##        return Pair(pair.getFirst() + self._x, pair.getSecond() + self._y)
        





    def __add__(self, pair):
        if isinstance(pair, Pair):
            return Pair(pair.getFirst() + self._x, pair.getSecond() + self._y)
        else:
            raise TypeError('cannot add '+type(pair).__name__+ ' to a Pair instance')
        










    def __mul__(self, scalar):
        if not (isinstance(scalar, int) or isinstance(scalar, float)):
            raise TypeError('invalid type for Pair')
        return Pair(scalar * self._x, scalar * self._y)
        








    def __eq__(self, pair):
        if(isinstance(pair, Pair)):
            return pair.getFirst() == self._x and pair.getSecond() == self._y
        else:
            return False

    def __ne__(self, pair):
        if(isinstance(pair, Pair)):
            return pair.getFirst() != self._x or pair.getSecond() != self._y
        else:
            return True












    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('Pair indices must be integers, not '+type(index).__name__)
        
        if index == 0:
            return self._x
        elif index == 1:
            return self._y
        else:
            raise IndexError('Pair index out of range')
        

    def __setitem__(self, index, value):
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError('invalid type for Pair')
        
        if not isinstance(index, int):
            raise TypeError('Pair indices must be integers, not '+type(index).__name__)
        
        if index == 0:
            self._x = value
        elif index == 1:
            self._y = value
        else:
            raise IndexError('Pair index out of range')

        
            
    def __del__(self):
        Pair._instances -= 1


    @staticmethod
    def centroid(pairs):
        length = len(pairs)
        if length <= 0:
            raise ValueError('Empty list, pairs must contain at least one Pair instance.')
        else:
            p = Pair()
            for pair in pairs:
                p += pair

            return p * (1.0/length)
                             
