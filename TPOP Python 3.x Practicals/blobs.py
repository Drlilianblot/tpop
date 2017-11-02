'''
Created on 22 Nov 2016

@author: Lilian
'''

cell_image = [
         [0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 1, 0, 0],
         [1, 1, 1, 0, 1, 1, 1, 0],
         [1, 0, 1, 0, 0, 1, 1, 0],
         [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 1]
         ]

def get_cell(image, x, y, neighbourhood=8):
    """
    One of the important issue in this exercise is that if we are not 
    careful we may create an infinite recursive call. Let consider the
    pixel (x,y). the pixel (x-1,y) is one of its neighbour,therefore it
    may call get_cel(image, x-1, y). So this time it will consider the
    neighbourhood around pixel (x-1,y). (x,y) is one of (x-1,y)
    neighbours, and it may call again get_cell(image, x, y), ending up
    where it started. It will keep switching between the two pixels until
    it run out of memory.
    The solution is to have a data structure to keep track of the pixels
    visited. I choose a list of tuple containing the coordinate of pixels
    visited, e.g. [(1,1),(3,2),..]. 
    Note there are other way to do that, for example a 2D list of boolean
    of the same size as the image. If the value visited[x][y] is True, 
    the pixel (x,y) has been visited/processed.
    So why not pass visited as a parameter? It simply a design decision.
    I am writing a code library that could be used by other programmers,
    therefore It must be simple and easy to use. I should hide the details
    of the implementation. Users of my API should not know that I need to
    use a 'visited' variable. If they want to get the cell they should
    only provide the relevant information, image, pixel and neighbourhood.
    We could use a global variable for visited, but again this is a very
    bad practice.
    The solution is to define another function that will have the needed
    parameter visited, and have get_cell(...) calling this function. We 
    could define this new function at the same level as get_cell(...), 
    or even better use the ability to define a function inside a function
    as shown below.
    """
    def cell_rec(x, y, visited, image, neighbours):
        """
        This is the function that do all the hard work. Note the added
        parameter 'visited'. It will store the pixel from the cell that
        have been already processed/visited.
        """
        try:
            if (x >= 0 and y >= 0 
                and image[y][x] == 1  
                and (x, y) not in visited): # be careful with coordinate 
                # system and internal representation pixel (x,y) is at
                # image[y][x].
                visited.append((x, y))  
                
                # now process the neighbours           
                for neighbour in neighbours:
                    cell_rec(x + neighbour[0], y + neighbour[1], visited, 
                             image, neighbours)
            
            # ELSE means that we are out of bounds, or the pixel has already 
            # been processed, or the pixel is not part of a cell.
            
        except IndexError:
            # out of bounds so ignore 
            pass
        
    # rather than using a series of nested for loops, with 
    # condition to check if we are not processing (x,y) again,
    # I prefer to pass the neighbourhood as a list of offset
    # values. By doing so I can use the same looping structure 
    # for any neighbourhood types, as long as it is passed as
    # a list of tuples.    
    if neighbourhood == 8:
        neighbours = [(-1, -1), (-1, 1), (1, -1), (1, 1),
                      (-1, 0), (1, 0), (0, -1), (0, 1)]
    elif neighbourhood == 4:
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    else:
        raise ValueError("Neighbourhood expected values are 8 or 4.")
    
    visited = [] # at the start I haven't visited any pixels
    
    # now I can call the recursive function I have just defined. It 
    # will grow the list of pixel from the seed (x,y).
    cell_rec(x, y, visited, image, neighbours)
    
    # The function has visited all possible pixel from the cell so
    # I return the list 'visited'.
    return visited

def cell_size(image, x, y, neighbourhood=8):
    return len(get_cell(image, x, y, neighbourhood))

def get_all_cells(image, neighbourhood=8):
    label = 0
    visited = []
    all_cells = {}
    for row in range(len(image)):
        for col in range(len(image[row])):
            if (col, row) not in visited:
                cell = get_cell(image, col, row, neighbourhood)
                if cell:  # there is a cell at (col,row)
                    visited += cell
                    all_cells[label] = cell
                    label += 1
                else:  # no cell at that position
                    visited.append((col, row))
    
    return all_cells

def get_average_cell(image, neighbourhood=8):
    all_cells = get_all_cells(image, neighbourhood)
    if all_cells:
        totalSize = 0
        for cells in all_cells.values():
            totalSize += len(cells)
            
        return totalSize / len(all_cells)
    else:
        return 0
                
    
if __name__ == '__main__':
    print(get_cell(cell_image, 0, 1))
    print(cell_size(cell_image, 0, 1))
    print(get_all_cells(cell_image, 8)) 
    print(get_average_cell(cell_image, 8)) 
                        
