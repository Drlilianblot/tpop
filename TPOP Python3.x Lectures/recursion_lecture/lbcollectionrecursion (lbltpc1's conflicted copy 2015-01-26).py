'''
Created on 20 Jan 2015

@author: lb1008
'''
import abc # library for abstract classes

class AbstractCollection(object):
    '''This class provides a skeletal implementation of the Collection interface.'''
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        self._size = 0
        
    @abc.abstractmethod
    def add(self,element):
        ''' add element to the collection'''
        
        
    @abc.abstractmethod
    def clear(self):
        ''' Removes all elements from the collection'''
        
    def isempty(self):
        return self._size == 0
    
    @abc.abstractmethod
    def pop(self):
        ''' Returns and removes the first element from the collection'''
        
    @abc.abstractmethod
    def peek(self):
        ''' Returns the first element from the collection'''
    
    @abc.abstractmethod
    def __contains__(self, element):
        ''' Returns True if element is in the collection'''
        
    def __len__(self):
        ''' Returns the number of elements in the collection'''
        return self._size
        

class LinkedQueue(AbstractCollection):

    ## inner class, watch the indentation
    ## internal representation using linked structure
    class _Node: 
        def __init__(self, data, nextNode):
            self.data = data
            self.next = nextNode

        def __repr__(self):
            return ('<Node:'+ str(self.data)+ '>')

    def __init__(self):
        '''Construct an empty queue'''
        super(LinkedQueue, self).__init__()
        self._head = None # a Node object
        self._tail = None # a Node object

    def add(self, element):
        '''Add element at the end of the queue'''
        new_node = LinkedQueue._Node(element, None)
        if self._size == 0:
            self._tail = new_node
            self._head = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def clear(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def pop(self):
        '''Returns and removes the element at the front of the queue'''
        front_node = self._head
        self._head = self._head.next
        self._size -= 1    
        return front_node.data

    def peek(self):
        '''Returns the element at the front of the queue'''
        return self._head.data

    def __contains__(self, element):
        return self._contains_recursion(element, self._head)
    
    def _contains_recursion(self, element, node):
        if node is None:
            return False
        elif (element == node.data):
            return True
        else:
            return self._contains_recursion(element, node.next)
    
    
    def __str__(self):
        output =  'queue:'+ '<'
        currentNode = self._head 
        while currentNode is not None:
            output +=  str(currentNode.data) +', '
            currentNode = currentNode.next 
        output += '>'
        return output

    

##################################
##         TESTS
##################################
    
queue = LinkedQueue()
print queue
print "add 3:"
queue.add(3)
print queue
queue.add(5)
print queue
queue.add(1)
print queue
queue.add(1)
print queue
queue.add(3)
print queue
 
print 'contains 3?', 3 in queue
print 'contains 13?', 13 in queue
 
print 'pop:',queue.pop(),'->',queue
print 'peek:',queue.peek(),'->',queue
queue.add(4)
print queue
queue.clear()
print queue



