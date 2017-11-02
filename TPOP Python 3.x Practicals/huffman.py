'''
Created on 17 Nov 2016

@author: lb1008
'''

class HuffmanTree(object):
    '''
    classdocs
    '''


    def __init__(self, left = None, right = None, symbol = None, frequency = 0):
        '''
        Constructor
        '''
        self._right = right
        self._left = left
        self._frequency = frequency
        self._symbol = symbol
        self._encoding = None
        
    def __str__(self):
        if self._symbol is None:
            symbol = "*"
        else:
            symbol = self._symbol
            
        if self._left is None and self._right is None: # a leaf
            return ("<("+str(symbol) + ":" + str(self._frequency) +")>") 
        else:
            return ("<("+str(symbol) + ":" + str(self._frequency) +") " 
                        + str(self._left)+ " | " + str(self._right) + ">")

    def __repr__(self):
        return self.__str__()
        
    def _get_frequency(self):
        return self._frequency
    
    def build_tree(self, frequencies):
        leaves = []
        for symbol in frequencies:
            leaves.append(HuffmanTree(symbol = symbol, frequency = frequencies[symbol]))
            
        tree = self._build_tree(leaves)
        self._right = tree._right
        self._left = tree._left
        self._frequency = tree._frequency
        self._symbol = tree._symbol
            
    def _build_tree(self, list_tree):
        if not list_tree:
            raise ValueError("need at least one tree in the list!")
        elif len(list_tree) == 1:
            print("end recursion", list_tree)
            return list_tree[0]
        else:
            sorted_trees = sorted(list_tree, key = HuffmanTree._get_frequency, reverse = True)  
            print(sorted_trees)
            left = sorted_trees.pop()
            right = sorted_trees.pop()
            tree = HuffmanTree(left = left, right = right, frequency = left._frequency + right._frequency)
            sorted_trees.append(tree)
            return self._build_tree(sorted_trees)
        
    
    def _is_leaf(self):
        return self._left is None and self._right is None
        
    
    def get_encoding(self):
        
        def _build_encoding_rec(tree, dico, code):
            if tree._is_leaf():
                dico[tree._symbol] = code
            if tree._left is not None:
                _build_encoding_rec(tree._left, dico, code+"0")
            if tree._right is not None:
                _build_encoding_rec(tree._right, dico, code+"1")
          
        if self._encoding is None:      
            self._encoding = {}
            _build_encoding_rec(self, self._encoding, "")

        return self._encoding
                
     
    def encode(self,word):
        output = ""
        if self._encoding is None:
            self.get_encoding()
            
        for symbol in word:
            output += self._encoding[symbol]        
        
        return output
                
        
    def decode(self, code):
        output = ""
        def _decode(tree, code):   
            if tree._is_leaf():
                return code, tree._symbol
            elif code == "":
                raise ValueError("invalid code entry!")
            elif code[0] == "0":
                return _decode(tree._left, code[1:])  
            elif code[0] == "1":
                return _decode(tree._right, code[1:])  
        
        while code != "":
            code, symbol = _decode(self, code)
            output += symbol
            
        return output


tree = HuffmanTree()
tree.build_tree({"a":3, "b":2, "c":2, "d":3})  
print(tree)
print(tree.get_encoding())    
print(tree.encode("abcd")) 
print(tree.decode(tree.encode("abcd")))
print(tree.decode("1000011"))
 
