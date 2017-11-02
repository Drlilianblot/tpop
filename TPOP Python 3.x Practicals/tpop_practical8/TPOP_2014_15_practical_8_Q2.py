'''
Created on 13 Jan 2015

@author: Lilian
'''

class Item(object):
    
    def __init__(self, barcode, name, ppu, vat, description = '', units = 1):
        self._uid = barcode
        self._name = name
        self._desc = description
        self._units = units
        self._ppu = ppu
        self._vat = vat
        
    def get_barcode(self):
        return self._uid
    
    def get_name(self):
        return self._name
    
    def get_description(self):
        return self._desc
    
    def get_units(self):
        return self._units
    
    def get_ppu(self):
        return self._ppu
    
    def get_vat(self):
        return self._vat
    
    def get_item_price(self):
        return self._ppu * self._units * (1 + self._vat)
    
    def set_ppu(self, new_ppu):
        self._ppu = new_ppu
        
    def set_vat(self, new_vat):
        self._vat = new_vat
        
    def __str__(self):
        output = self.get_name()+'('+self.get_barcode()+'):\n'
        output += '\t       units: '+str(self.get_units())+'\n'
        output += '\t   price ($): '+str(self.get_item_price())+'(incl. '+str(self.get_vat()*100)+'% vat)\n'
        return output

class Clothing(Item):
    
    def __init__(self, barcode, name, ppu, vat, size, description = '', units = 1):
        super(Clothing, self).__init__(barcode, name, ppu, vat, description, units)
        self._size = size
        
    def get_size(self):
        return self._size
    
    def __str__(self):
        output = super(Clothing, self).__str__()
        output += '\t        size: '+str(self.get_size())+'\n'
        output += '\t description: '+self.get_description() + '\n'
        return output
    
class Electronic(Item):
    
    def __init__(self, barcode, name, ppu, vat, brand, warranty, description = '', units = 1):
        super(Electronic, self).__init__(barcode, name, ppu, vat, description, units)
        self._brand = brand
        self._warranty = warranty
        
    def get_brand(self):
        return self._brand
    
    def get_warranty(self):
        return self._warranty
    
    def set_warranty(self, warranty):
        self._warranty = warranty
        
    def __str__(self):
        output = super(Electronic, self).__str__()
        output += '\t    warranty: %1d year(s)\n'% self.get_warranty()
        output += '\t description: '+self.get_description() + '\n'
        return output
        
class Basket(object):
    
    def __init__(self):
        self._content = {} # keys are item barcode, values are tuples (quantity,item objects) of that item
        self._items = {} # keys are item barcode, values are item objects
        
    def add_item(self, item, quantity = 1):
        if item.get_barcode() in self._content:
            data = self._content[item.get_barcode()]
            self._content[item.get_barcode()] = (data[0] + quantity, data[1])
        else:
            self._content[item.get_barcode()] = (quantity, item)
            
    def remove_item(self, item, quantity = 1):
        if item.get_barcode() in self._content:
            data = self._content[item.get_barcode()]
            new_quantity = data[0] - quantity
            if new_quantity < 0:
                raise ValueError('Invalid quantity, not enough items in the basket.')
            elif new_quantity > 0:
                self._content[item.get_barcode()] = (new_quantity, data[1])
            else: # no more item of that type (new_quantity == 0), so remove completely from basket
                self._content.pop(item.get_barcode())                
        else:
            raise ValueError('No such item.')
        
    def remove_all(self, item):
        if item.get_barcode() in self._content:
            self._content.pop(item.get_barcode())
                
        else:
            raise ValueError('No such item.')
        
    def get_price(self):
        price = 0
        for item in self._content:
            data = self._content[item]
            price += data[0] * data[1].get_item_price()
            
        return price
    
    def __str__(self):
        output = 'BASKET content:\n'
        header = '| %-15s | %4s | %10s | %10s |\n'%('Products', 'Qty', 'Unit Price', 'Price')
        output += '-' * (len(header)-1) +'\n'
        output += header
        output += '-' * (len(header)-1) +'\n'
        
        for data in self._content.values():
            output += '| %-15s | %4d | %10.2f | %10.2f |\n'%( data[1].get_name(),data[0],data[1].get_item_price(),data[1].get_item_price()*data[0]) 
            
        output += '-' * (len(header)-1) +'\n'
        output += '  %15s | %17s | %10.2f |\n'%('','Total bill: $', self.get_price())
        output += ' ' * 18 + '-' * (len(header)-19) +'\n'
           
        return output       
    
    
    
            