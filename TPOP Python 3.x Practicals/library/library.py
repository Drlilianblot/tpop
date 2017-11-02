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

        ## TODO define what are the neccessary mutator methods

    ## Convenience methods

        ## TODO is there any other methods that could be useful?


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



class Library:
    """

    """

    def __init__(self):
        ## TODO
        pass

    ## I am taking great care in writing the method __str__. It should display the necessary
    ## information about the state of the object Library. In addition it should format the
    ## string in such a way that all information is easily readable.
    def __str__(self):
        ## TODO
        pass

    def __repr__(self):
        ## TODO
        pass

    def add_member(self, member):
        ## TODO
        pass

    def create_member(self, firstname, surname, postcode, uid):
        ## TODO
        pass


    def add_item(self, item):
        ## TODO
        pass


    def create_item(self, title, author, media, uid):
        ## TODO
        pass


    def borrow(self, item_uid, member_uid):
        ## TODO
        pass

    def delete_item(self, item_uid):
        ## TODO
        pass


    def delete_member(self, member_uid):
        ## TODO
        pass

    def get_member(self, uid):
        '''
            Returns the member with the corresponding uid, raise a KeyError if the
            member does not exist.
        '''
        ## TODO
        pass
    
    def get_members(self):
        '''
            Returns all the member in the library.
        '''
        ## TODO
        pass

    def get_item(self, uid):
        '''
            Returns the item with the corresponding uid, raise a KeyError if the
            item does not exist.
        '''
        ## TODO
        pass
        
    def get_items(self):
        '''
            Returns all the items in the library.
        '''
        ## TODO
        pass
        
    def return_item(self, item_uid):
        '''
        returns True if an item has been successfully returned,
        False otherwise. You may want to use Exception instead
        of returning True or False.

        '''
        ## TODO
        pass            



