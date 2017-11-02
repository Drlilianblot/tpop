
class BSTree:

    ## ------------------Internal representation ----------------##
    class _Node:

        def __init__(self, key, data):
            assert key is not None, 'BST_Node constructor: Illegal key = None Argument '
            self._key = key
            self._data = data
            self._left = None
            self._right = None

        def __repr__(self):
            return '<' + str(self._key) + ' : ' + str(self._data) +'>'


        def key(self):
            return self._key

        def getData(self):
            return self._data

        def getLeft(self):
            return self._left

        def getRight(self):
            return self._right

        def setData(self, data):
            self._data = data

        def setLeft(self, bstNode):
            self._left = bstNode

        def setRight(self, bstNode):
            self._right = bstNode

        def isleaf(self):
            return (self._left is None and self._right is None)
        
    ## ----------------End Internal representation --------------##


        

    def __init__(self, bst_node = None):
        self._root = bst_node ## an empty Tree is a tree where _root is None

    def isempty(self):
        return self._root is None

    def getLeftTree(self):
        """
        returns the root's left branch as a BSTree object, None if the root
        has no left child.
        """
        if self.isempty(): return None
        return BSTree(self._root.getLeft())

    def getRightTree(self):
        """
        returns the root's right branch as a BSTree object, None if the root
        has no right child.
        """
        if self.isempty(): return None
        return BSTree(self._root.getRight())

    def hasLeftBranch(self):
        """
        returns True is the root has a left branch, False otherwise
        """
        if self.isempty(): return False
        return self._root._left is not None

    def hasRightBranch(self):
        """
        returns True is the root has a right branch, False otherwise
        """
        if self.isempty(): return False
        return self._root._right is not None

    def getRootData(self):
        if self.isempty(): return None
        return self._root._data

    def getRootKey(self):
        if self.isempty(): return None
        return self._root._key

    def setLeftBranch(self, bst):
        """
        set the left branch of the tree with the BSTree bst. Note that bst is a BSTree object
        not a _Node object.
        """
        if self.isempty():
            raise Exception("Invalid operation: cannot set left branch of empty BST")

        self._root._left = bst._root

    def setRightBranch(self, bst):
        """
        set the right branch of the tree with the BSTree bst. Note that bst is a BSTree object
        not a _Node object.
        """
        if self.isempty():
            raise Exception("Invalid operation: cannot set right branch of empty BST")

        self._root._right = bst._root


    def insertIterative(self, key, data):
        """
        iterative sample code to insert a data associated with a key
        """
        if self.isempty():
            self._root = self._Node(key,data)
        else:
            currentNode = self._root
            while True:
                if(currentNode.key() == key):
                    currentNode.setData(data)
                    break

                elif(currentNode.key() > key):
                    if(currentNode.getLeft() is None):
                        currentNode.setLeft(self._Node(key,data))
                        break
                    else:
                        currentNode = currentNode.getLeft()

                else:
                    if(currentNode.getRight() is None):
                        currentNode.setRight(self._Node(key,data))
                        break
                    else:
                        currentNode = currentNode.getRight()



    ########################################
    ##            EXERCISES               ##
    ########################################
 
    def printInOrder(self):
        """
        return the content of the BST in order (in order means in Keys ascending order).
        """
        if self.isempty(): return "#"
        
        result = '{'

        ## PrintInOrder left child
        result += self.getLeftTree().printInOrder()+ ','

        ## PrintInOrder current root
        result += str(self._root) + ','
        
        ## PrintInOrder right child
        result += self.getRightTree().printInOrder()+ '}'

        return result
    
    def insert(self, key, data):
        """
        method that insert the data element in the BST using the key.
        The method should be recursive
        """
        if self.isempty():
            self._root = self._Node(key,data)
            return self
        
        if self._root.key() == key:
            self._root.setData(data)
            return self
            
        elif self._root.key() > key:
            self.setLeftBranch(self.getLeftTree().insert(key,data))
            return self
                
        else: ## self._root.key() < key:
            self.setRightBranch(self.getRightTree().insert(key,data))
            return self

    def get(self, key):
        """
        method that returns the data element in the BST associated with the key.
        If the key does not exist, the method returns None.
        The method should be recursive
        """
        if self.isempty():
            return None
        
        if self._root.key() == key:
            return self._root.getData()
            
        elif self._root.key() > key:
            return self.getLeftTree().get(key)
                
        else: ## self._root.key() < key:
            return self.getRightTree().get(key)

    def hasKey(self, key):
        """
        returns true if the BST contains the key, false otherwise
        """
        if self.isempty():
            return False
        
        if self._root.key() == key:
            return True
            
        elif self._root.key() > key:
            return self.getLeftTree().hasKey(key)
                
        else: ## self._root.key() < key:
            return self.getRightTree().hasKey(key)

    def contains(self, data):
        """
        returns true if the BST contains data, false otherwise
        """
        if self.isempty():
            return False
        
        if self._root.getData() == data:
            return True
            
        else: ## means if it's not the root check if it is in the right or left tree
            return (self.getLeftTree().contains(data) or
                    self.getrightTree().contains(data))

    def keys(self):
        """
        returns the list of keys in the BST, it must not have any duplicates.
        """
        if self.isempty():
            return []
                            
        else:
            list_keys = [self._root.key()]
            list_keys += self.getLeftTree().keys()
            list_keys += self.getRightTree().keys()
            return list_keys

    def values(self):
        """
        returns the list of values/data in the BST. They may be some duplicates
        """
        pass











########################################
##              TEST                  ##
########################################
                    
                    
                
##bst = BSTree(BSTree._Node(10, 'ten'))
bst = BSTree()
print bst.printInOrder()
print bst.keys()
print bst.get(11)
print bst.contains("onze")

bst.insert(13, 'treize')
bst.insertIterative(15, 'fiften')
bst.insertIterative(5, 'five')
bst.insertIterative(11, 'eleven')
bst.insertIterative(11, 'onze')
bst.insertIterative(9, 'neuf')
bst.insertIterative(3, 'three')
bst.insertIterative(2, 'onze')
bst.insert(6, 'six')
print bst.printInOrder()
print bst.keys()
print bst.get(11)
print bst.contains("onze")


