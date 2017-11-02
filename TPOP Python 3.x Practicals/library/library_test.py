from library import *

#######################################################
##
##                TESTS
##
#######################################################
        
local_library = Library()

print (local_library)

print ('Adding member :', local_library.create_member('lilian','blot','xxx', 'm007'))
print ('Adding member :', local_library.create_member('will','Smith','xxx', 'm001'))

try:
    print ('Adding member :', local_library.create_member('Alan','Sharpe','xxx', 'm001')) ## should not be added, existing uid
except Exception as err:
    print (err)
           
new_member = Member('Alan','Sharpe','xxx', 'm002')
print ('Adding member :', local_library.add_member(new_member)) ## should not be added, existing uid
    
print (local_library)

print ('Adding item :', local_library.create_item('Le grand bleu','J.L. Besson','DVD', 'ref007'))
print ('Adding item :', local_library.create_item('Le grand bleu','J.L. Besson','DVD', 'ref008'))

try:
    print ('Adding item :', local_library.create_item('Fawlty Towers','J. Cleese','DVD', 'ref008') )## should not be added, existing uid
except Exception as err:
    print (err)

print (local_library)

new_item = Item('Fawlty Towers','J. Cleese','DVD', 'ref010')
print ('Adding item :', local_library.add_item(new_item))
    
print ('\n\n 007 Borrowing ref008:', local_library.borrow('ref008', 'm007'))

print (local_library)

## Try to borrow same item twice before returning it
print ('\n\n 007 Borrowing ref008:', local_library.borrow('ref008', 'm007'))

print (local_library)
