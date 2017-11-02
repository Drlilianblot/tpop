class Member:

    def __init__(self, firstname, surname, postcode, uid):
        self._firstname = firstname ## assume should not be changed
        self._surname = surname      ## Can be changed (from maiden name)
        self._postcode = postcode    ## can be changed, member moved house
        self._uid = uid ## (str) a unique identifier, no two members have the same, cannot be changed
        self._borrowed = []  ## a list of items uid, can be changed only by using appropriate
                            ## methods, e.g. addBorrowedItem and removeBorrowedItem.

    def __str__(self):
        return ('<Member: uid = ' + self._uid + ', ' + self._firstname + ', ' +
                self._surname + ', ' +self._postcode + ', borrowed:' +str(self._borrowed) + '>')
    
    def __repr__(self):
        return ('Member("' + self._firstname  + '", "' + self._surname + '", ' +
                self._postcode+ '", ' + self._uid + '")')

    ## ACCESSORS
    def get_borrowed(self):
        '''
        Returns the list of the borrowed items' UID
        '''
        return self._borrowed

    def get_firstname(self):
        '''
        Returns the member's firstname
        '''
        return self._firstname
    
    def get_postcode(self):
        '''
        Returns the member's address postcode 
        '''
        return self._postcode
    
    def get_surname(self):
        '''
        Returns the member's surname 
        '''        
        return self._surname

    def get_UID(self):
        '''
        Returns the member's unique identifier (UID) 
        '''
        return self._uid

    ##MUTATORS
    def borrow_item(self, item_uid):
        '''
        Adds the item uid to the list of borrowed items. Raise an Exception
        if the item already in the list.
        '''
        if item_uid not in self._borrowed:
            self._borrowed.append(item_uid)
        else:
            raise Exception('Item already borrowed.')

    def return_item(self, item_uid):
        '''
        Removes the item uid from the list of borrowed items. Raise an Exception
        if the item is not in the list.
        '''
        if item_uid in self._borrowed:
            self._borrowed.remove(item_uid)
        else:
            raise Exception('No such Item.')

    def set_surname(self, new_name):
        '''
        Changes the member's surname to new_name
        '''        
        self._surname = new_name

    def set_postcode(self, new_postcode):
        '''
        Changes the member's postcode to new_postcode
        '''        
        self._postcode = new_postcode

    ## Convenience methods
    def has_items(self):
        '''
            Returns True if the member has some borrowed items, False otherwise.
        '''
        return not self._borrowed == []
    


class Item:
    ## TODO try to implement accessors and mutators in the same way as for the class
    ## Member.

    def __init__(self, title, author, media, uid):
        self._title = title
        self._author = author
        self._media = media
        self._uid = uid
        self._available = True  ## set to True if available, False otherwise
        self._member = None ## If borrowed contains borrower member uid, None otherwise

    def __str__(self):
        return ('<Item: uid = ' + self._uid + ', ' + self._title +
                ', available = ' + str(self._available) +
                ', borrower = ' + str(self._member) + '>')

    def __repr__(self):
        return ('Item("' + self._title  + '", "' + self._author + '", ' +
                self._media+ '", ' + self._uid + '")')


    ## ACCESSORS
    def get_UID(self):
        return self._uid

    def get_borrower(self):
        return self._member

    ## TODO implement the ramaining of the accessors.


    ## MUTATORS

    ## In order to keep the data consistent throughout the program, we do not
    ## provide a mutator for _available and _member. To modify them we have to
    ## call borrowItem of returnItem. This will ensure that these two instance
    ## variables are always in sync, e.g. if _available is True then _member is
    ## None, if _available is False then _member is not None, and vice versa.
    ##
    ## No other mutators should be provided, as we should not be able to change
    ## the title.
    ## One could ask, what if there is an error in the title and we want to change
    ## it? In that case we delete the item and create a new one with the correct
    ## title. It may look costly to do that, but this is a very small price to pay
    ## for keeping data consistent.
    def borrow_item(self, memberUID):
        if self.isavailable() and self._member is None:
            self._available = False
            self._member = memberUID
        else:
            raise Exception("Item is currently borrowed.")

    def return_item(self):
        if self.isavailable() or self._member is None:
            raise Exception("Item is not currently borrowed.")
        else:
            self._available = True
            memberUID = self._member
            self._member = None
            return memberUID
        
    
    ## Convenience methods
    ## It can be useful to add additional method to make your code easier to
    ## read, and your object easier to use. Below is such a method.
            
    def isavailable(self):
        '''
            Returns True if the item is available, False otherwise.
        '''
        return self._available == True



class Library:
    """

    Attributes:
    - members: a Dictionary containing Member.uid as key and Member object as value
    - items:   a Dictionary containing Item.uid as key and Item object as value
    """

    def __init__(self):
        self._members = {} ## Dictionary containing Member.uid as key and Member object as value
        self._items = {} ## Dictionary containing Item.uid as key and Item object as value


    ## I am taking great care in writing the method __str__. It should display the necessary
    ## information about the state of the object Library. In addition it should format the
    ## string in such a way that all information is easily readable.
    def __str__(self):
        output = '\n\n Library:\n'
        output += ' - Members:\n'
        for member in self.get_members():
            output += '\t' + str(member) +'\n'

        output += ' - Items:\n'
        for item in self.get_items():
            output += '\t' + str(item) + '\n'

        return output

    def __repr__(self):
        return ('<Library: \n member::'+ str(self._members) + '\n items::' +str(self._items) +'\n>')


    def add_member(self, member):
        '''
        Adds a Member object to the library. Raises an Exception if a member with the same
        uid already exists.       
        '''
        if member.get_UID() in self._members: ## uid already existing so must not add item
            raise Exception('A member with same UID already in the library.')
        else:
            self._members[member.get_UID()] = member

    def create_member(self, firstname, surname, postcode, uid):
        '''

        creates and add a member to the library. Returns the Member object if it is created,
        raises an Exception  if the uid already exists.
        
        '''
        if uid in self._members: ## uid already existing so must not add item
            raise Exception('A member with same UID already in the library.')
        else:
            member = Member(firstname, surname, postcode, uid)
            self._members[uid] = member
            return member


    def add_item(self, item):
        '''
        Adds an Item object to the library. Raises an Exception if an item with the same
        uid already exists.       
        '''
        if item.get_UID() in self._items: ## uid already existing so must not add item
            raise Exception('An item with same UID already in the library.')
        else:
            self._items[item.get_UID()] = item


    def create_item(self, title, author, media, uid):
        '''

        creates and add an item to the library. Returns the item if it is created,
        raises an Exception if the uid already exists.
        
        '''
        if uid in self._items: ## uid already existing so must not add item
            raise Exception('An item with same UID already in the library.')
        else:
            item = Item(title, author, media, uid)
            self._items[uid] = item
            return item




    def borrow(self, item_uid, member_uid):
        '''
        returns True if an item has been successfully borrowed,
        False otherwise. You may want to use Exception instead
        of returning True or False.

        '''
        if (item_uid in self._items and
           member_uid in self._members):
            item = self._items[item_uid]
            if item.isavailable():         
                member = self._members[member_uid]

                try:
                    member.borrow_item(item_uid)
                except Exception:
                    return False
                else:        
                    item.borrow_item(member_uid)    ## MUST BE CHANGED USING METHOD YOU PROVIDED IN CLASS ITEM
                    return True
                
            else: ## item is not available so cannot be borrowed
                return False  # probably should raise an error
        else: ## item or member do not exist so cannot be borrowed
            return False  # probably should raise an error

    def delete_item(self, item_uid):
        '''
        returns the item if has be successfully deleted,
        None otherwise, e.g. item is still borrowed or does not exist.
        You may want to use Exception instead.
        '''
        if item_uid in self._items:
            item = self.get_item(item_uid)
            if item.isavailable():
                del self._items[item_uid]
                return item
            else:
                return None # probably should raise an error
        else:
            return None # probably should raise an error
            
        


    def delete_member(self, member_uid):
        '''
        returns True if an member has been successfully deleted,
        False otherwise, e.g. member has still some borrowed items or does not exist.
        You may want to use Exception instead of returning True or False.
        
        If you decide that a member can be deleted even if he has some items in his\her
        possession, you must ensure that the borrowed items are also removed from the
        list of items to safeguard your data integrity. You will not be able to
        loan these items later on.
        '''
        ## TODO
        pass

    def get_member(self, uid):
        '''
            Returns the member with the corresponding uid, raise a KeyError if the
            member does not exist.
        '''
        return self._members[uid]
    
    def get_members(self):
        '''
            Returns all the member in the library.
        '''
        return self._members.values()

    def get_item(self, uid):
        '''
            Returns the item with the corresponding uid, raise a KeyError if the
            item does not exist.
        '''
        return self._items[uid]
        
    def get_items(self):
        '''
            Returns all the items in the library.
        '''
        return self._items.values()
        
    def return_item(self, item_uid):
        '''
        returns True if an item has been successfully returned,
        False otherwise. You may want to use Exception instead
        of returning True or False.

        '''
        ## TODO
        pass            



