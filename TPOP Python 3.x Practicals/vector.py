'''
Created on 15 Nov 2016

@author: Lilian
'''

from copy import deepcopy

class Vector(object):
    ''' Some docs-string to explain the class Vector'''
    
    def __init__(self, data = None):
        ''' some doc-string to explain how to create an instance of the class 
        vector'''
        self._vector = []
        if(data is not None):
            # ensure that the data contains representation of float, either as 
            # a float itself or as an int or a string. This will raise an error
            # if the format is incorrect.
            # In addition this makes a copy of the initial list passed in the
            # parameter.
            for value in data:
                self._vector.append(float(value))
                 
                
    def __str__(self):
        if len(self._vector) == 0:
            return '[]'
        else:
            output = "["
            for value in self._vector[:-1]:
                output += str(value) +', '
            
            output += str(self._vector[-1]) + ']'
            return output
        
    def __repr__(self):
        return self.__str__()
        
    
    def dim(self):
        ''' add some doc-string'''
        return len(self._vector)   
    
    
    def get(self, index):
        return self._vector[index]
    
    
    def set(self, index, value):
        if not isinstance(value, float):
            raise TypeError('float required')
        
        self._vector[index] = value
        
    
    def scalar_product(self, scalar):
        ''' add some doc-string'''
        product = []
        for value in self._vector:
            product.append(scalar * value)
        
        # from the created list, create a new Vector instance using the 
        # class' constructor
        new_vector = Vector(product)
        return  new_vector


    def add(self, other):
        ''' add some doc-string'''
        if not isinstance(other, Vector):
            raise TypeError('Invalid parameter type, must be Vector')
        elif self.dim() != other.dim():
            raise ValueError("size of vectors are incompatible")
        
        result = []
        for index in range(self.dim()):
            result.append(self._vector[index] + other._vector[index])
            
        return Vector(result) 
    
    
    def __add__(self, other):
        return self.add(other)
    
    
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('Invalid parameter type, must be Vector')
        elif self.dim() != other.dim():
            raise ValueError("size of vectors are incompatible")
        
        
        for index in range(self.dim()):
            self._vector[index] += other._vector[index]
            
        return self
    
    
    def __rmul__(self, scalar):
        return self.scalar_product(scalar)
    
    
    def __eq__(self, other_vector):
        if not isinstance(other_vector, Vector):
            return False
        if self.dim() != other_vector.dim():
            return False
        for index in range(self.dim()):
            if self.get(index) != other_vector.get(index):
                return False
            
        return True
    
    
    @classmethod
    def factory_from_text(cls, text):
        elements = text.split()
        values = []
        for element in elements:
            values.append(float(element))
        
        return cls(values)

    @classmethod
    def factory_from_csv(cls, text):
        elements = text.split(',')
        values = []
        for element in elements:
            values.append(float(element))
        
        return cls(values)
    
    @staticmethod
    def centroid(vectors):
        if vectors == []:
            raise ValueError(" list must not be empty.")
        else:
            result = deepcopy(vectors[0])
            print(type(result))
            for index in range(1, len(vectors)):
                result += vectors[index]
            
            return 1/len(vectors) * result



        
###### TESTS ########################
a_vector = Vector([1,2,3])
vector1 = deepcopy(a_vector)
print("a_vector", a_vector, a_vector.dim())
print("vector1",vector1, vector1.dim())
print("a_vector == vector1",  a_vector == vector1)
vector2 = a_vector.scalar_product(10)
print("Vector2", vector2, vector2.dim())
print("vector2 != vector1",  vector2 != vector1)
a_vector += vector2
print("result of +=", a_vector)
print("result of *", 11 * a_vector)
print("result of +", a_vector + vector2)
print("From text:", Vector.factory_from_text("1 1.0 2.3 0"))
print("From csv:", Vector.factory_from_csv("1, 1.0, 2.3 ,0 \n"))

vectors = [Vector([1,1]), Vector([-1,1]), Vector([1,-1]), Vector([-1,-1])]
print("Centroid of", vectors, "is:",Vector.centroid(vectors))