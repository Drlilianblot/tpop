'''
Created on 17 Nov 2016

@author: Lilian
'''
from bst import BST

tree = BST()
print(tree)
tree.put(7,  'T')
tree.put(4,  'A')
tree.put(15, 'E')
tree.put(1,  'S')
tree.put(3,  'T')
tree.put(8,  'R')
tree.put(19, 'K')
tree.put(5,  'R')
print(tree)
print(" get 5 =", tree.get(5))
print(7 in tree)
print(0 in tree)

print(tree.has_value("T"))

print(tree.has_value("b"))

print(tree.keys())
print(tree.values())
