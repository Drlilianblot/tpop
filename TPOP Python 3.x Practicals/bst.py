'''
Created on 17 Nov 2016

@author: Lilian
'''

class BST(object):
    '''
    classdocs
    '''


    def __init__(self, key = None, value = None):
        '''
        Constructor
        '''
        self._key = key
        self._value = value
        self._left = None
        self._right = None
        
        
    def __str__(self):
        output = ("<" + str(self._left) + ", " 
                  +str((self._key, self._value)) +", "
                  + str(self._right) + ">")
        return output
    
    
    def __repr__(self):
        return self.__str__()
        
        
    def _has_left_child(self):
        return self._left is not None
    
    
    def _has_right_child(self):
        return self._right is not None
    
    
    def _is_leaf(self):
        return self._left is None and self._right is None

    def isempty(self):
        return (self._key is None
                and self._left is None
                and self._right is None)


    def __contains__(self, key):
        if self.isempty():
            return False
        
        if self._is_leaf():
            return key == self._key
        else:
            if key == self._key:
                return True
            elif key < self._key:
                return (self._has_left_child() and
                        key in self._left)
            else:
                return (self._has_right_child() and
                        key in self._right)


    def has_value(self, value):
        if self.isempty(): # empty tree
            return False

        if self._value == value:
            return True
        else:
            # search the left branch
            if self._has_left_child():
                if self._left.has_value(value):
                    return True
                
            # not in the left branch    
            if self._has_right_child():
                return self._right.has_value(value)

            # not in the right branch
            return False


    def keys(self):
        if self.isempty(): # empty tree
            return []
        
        output = []
        if self._has_left_child():
            output += self._left.keys()

        output.append(self._key)

        if self._has_right_child():
            output += self._right.keys()

        return output
    
    
    def put(self, key, value):
        if key is None:
            raise ValueError("None-Type not accepted as key.")
        
        if self.isempty(): 
            self._key = key
            self._value = value
            
        elif key == self._key: # update the mapping
            self._value = value
            
        elif key < self._key: # must be added to left branch
            if self._has_left_child():
                self._left.put(key, value)
            else:# if no branch create a new one with the (key, value) pair
                tree = BST(key, value)
                self._left = tree
        else:
            if self._has_right_child():# must be added to right branch
                self._right.put(key, value)
            else: # if no branch create a new one with the (key, value) pair
                tree = BST(key, value)
                self._right = tree
                
    def get(self, key):
        if key is None:
            raise ValueError("None-Type not accepted as key.")
        
        if self.isempty():
            raise KeyError("mapping key not found.")
        
        if key == self._key:
            return self._value
        
        elif key < self._key:
            if self._has_left_child():
                return self._left.get(key)
            
        else:
            if self._has_right_child():
                return self._right.get(key)
        
        # if we get here, it means that we did not find the key
        raise KeyError("Unknown key " + str(key))
        


    def values(self):
        if self.isempty(): # empty tree
            return []
        
        output = []
        if self._has_left_child():
            output += self._left.values()

        output.append(self._value)

        if self._has_right_child():
            output += self._right.values()

        return output

