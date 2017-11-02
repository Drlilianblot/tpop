'''
Created on 12 Jan 2016

@author: Lilian
'''
from shopping_app import *

item1 = Clothing('0001', 'CK shirt', 10, 0.1, 'M','a white shirt')
print(item1)

item2 = Clothing('0002', 'CK trouser', 20, 0.1, '31', 'a black trouser')
print(item2)

item3 = Clothing('0003', 'CK socks', 1, 0.1, '7-9', 'white pair of socks',units=3)
print(item3)

item4 = Clothing('0004', 'CK belt', 10, 0.1, '30-34', 'white belt')
print(item4)

item5 = Clothing('0005', 'CK gloves', 5, 0.1, '9', 'white glittery pair of gloves')
print(item5)

item6 = Clothing('0006', 'CK hat', 30, 0.1, '60', 'black hat')
print(item6)

item7 = Electronic('0007', '42" 4K TV', 3000, 0.2, 'Sony', 2, 'That is huge an saddly not affordable')
print(item7)

basket = Basket()
print('adding:', '1 x', item1.get_name())
basket.add_item(item1, 2)

print('adding:', '2 x', item2.get_name())
basket.add_item(item2, 2)

print('adding:', '10 x', item3.get_name())
basket.add_item(item3, 10)

print('adding:', '1 x', item4.get_name())
basket.add_item(item4, 1)

print('adding:', '2 x', item5.get_name())
basket.add_item(item5, 2)

print('adding:', '0 x', item6.get_name())
basket.add_item(item6, 0)

print('adding:', '3 x', item7.get_name())
basket.add_item(item7, 3)

print(basket)


print('remove:', '5 x', item3.get_name())
basket.remove_item(item3, 5)

print('remove:', 'all (3)', item7.get_name(), basket.remove_all(item7))

print('remove:', '0 x', item1.get_name())
basket.remove_item(item1, 0)

print(basket)
