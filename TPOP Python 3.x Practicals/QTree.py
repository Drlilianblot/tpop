'''
Created on 23 Nov 2016

@author: Lilian
'''

class BoundingBox(object):
    
    def __init__(self, x=0, y=0, width=0, height=0):
        if width < 0 or height < 0:
            raise ValueError("Invalid parameter")
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    
    def __contains__(self, element):
        if isinstance(element, tuple) and len(element) == 2:
            return (self.x + self.width > element[0] >= self.x 
                    and 
                    self.y + self.height > element[1] >= self.y)
        if isinstance(element, BoundingBox):
            return ((element.x,element.y) in self
                and (element.x, element.y + element.height -1) in self
                and (element.x + element.width -1, element.y) in self
                and (element.x + element.width -1, 
                    element.y + element.height -1) in self)
        raise TypeError(" invalid operation with " + str(type(element)))
        
    def __eq__(self, other):
        if not isinstance(other, BoundingBox):
            return False
        
        return (self.x == other.x
                and self.y == other.y
                and self.height == other.height
                and self.width == other.width)
    
    def intersect(self, other):
        if not isinstance(other, BoundingBox):
            raise TypeError("intersect not valid for " + str(type(other)))
        
        return ((self.x,self.y) in other
                or (self.x, self.y + self.height -1) in other
                or (self.x + self.width -1, self.y) in other
                or (self.x + self.width -1, self.y + self.height -1) in other
                or (other.x,other.y) in self
                or (other.x, other.y + other.height -1) in self
                or (other.x + other.width -1, other.y) in self
                or (other.x + other.width -1, other.y + other.height -1) in self)

class Asset(object):
    
    def __init__(self, box, content):
        self._bounding_box = box
        self._content = content
        
    def __repr__(self):
        return str(self._content)
    
    def get_bounding_box(self):
        return self._bounding_box
    
    def get_content(self):
        return self._content
    
    def intersect(self, bounding_box):
        return bounding_box.intersect(self._bounding_box)
                
    def is_in_area(self, bounding_box):
        return self._bounding_box in bounding_box
        
class Region(object):
    DEFAULT_MAX_DEPTH = 5
    #_______________________________________________________
    # In the case of a root node "parent" will be None. The
    # "rect" lists the minx,minz,maxx,maxz of the rectangle
    # represented by the node.
    def __init__(self, bounding_box, parent = None, max_depth=DEFAULT_MAX_DEPTH):
        self._parent = parent
        self._max_depth = max_depth
        if parent == None:
            self._depth = 0
        else:
            self._depth = parent._depth + 1
            
        self._bounding_box = bounding_box
        
        self._assets = []

        self._sw = None
        self._nw = None
        self._se = None
        self._ne = None
        
        
    def add(self, asset):
        asset_box = asset.get_bounding_box()
        if asset_box not in self._bounding_box:
            return False
        
        if self._depth == self._max_depth:
            self._assets.append(asset)
            return True
        
        nw, ne, se, sw = self._get_subdivision()  
        if (asset_box not in nw and
            asset_box not in ne and
            asset_box not in sw and
            asset_box not in se):
            # asset covers more than one sub-region so must be added to
            # this level
            self._assets.append(asset)
            return True
        
        # if we are here, it means that we need to add the asset to one of
        # the four sub-quadrants. We must create the four quadrants if it has
        # not been done yet, e.g. the node is a leaf.        
        if self._is_leaf():
            self._nw = Region(nw, self)
            self._ne = Region(ne, self)
            self._sw = Region(sw, self)
            self._se = Region(se, self)

        if asset_box in nw:
            return self._nw.add(asset)            
        elif asset_box in ne:
            return self._ne.add(asset)
        elif asset_box in sw:
            return self._sw.add(asset)            
        else: # asset_box in se:
            return self._se.add(asset)
        
          
    def _get_subdivision(self):
        if (self._bounding_box.width <= 1 or
            self._bounding_box.height <= 1):
            raise RuntimeError("Cannot do subdivision, box too small.") 
        
        width = self._bounding_box.width//2
        height = self._bounding_box.heigh//2
        
        nw = BoundingBox(self._bounding_box.x,
                         self._bounding_box.y,
                         width,
                         height)
        
        ne = BoundingBox(self._bounding_box.x + width,
                         self._bounding_box.y,
                         width,
                         height)
        
        sw = BoundingBox(self._bounding_box.x,
                               self._bounding_box.y + height,
                               width,
                               height)

        se = BoundingBox(self._bounding_box.x + width,
                               self._bounding_box.y + height,
                               width,
                               height)
        
        return (nw, ne, se, sw)
                                  
                
    def _is_leaf(self):
        return (self._ne is None
                and self._nw is None
                and self._sw is None
                and self._se is None)
        
        
    def get_assets(self, area = None):
        assets = []
        if area is None:
            assets += self._assets
        elif not area.intersect(self._bounding_box):
            return assets
        else:
            # the area intersect this node, so need to have a closer look
            # and check every assets from this node individually to see 
            #if it intersect the area.
            for asset in self._assets:
                if asset.intersect(area):
                    assets.append(asset)   
                   
        if not self._is_leaf():
            # if it is not a leaf, had the assets from the children
            assets += self._ne.get_assets(area)
            assets += self._nw.get_assets(area)
            assets += self._se.get_assets(area)
            assets += self._sw.get_assets(area)
            
        return assets
    
        
        
