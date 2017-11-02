try:
    dataFile = open('Data/precipitations-europe.txt')
except IOError as err:
    print ('The following error occurred:',err)
else:
    data = dataFile.readlines()
    dataFile.close() # we have read the full content of the file so we can close it
    minPrecipitation = []
    maxPrecipitation = []
    averagePrecipitation = 0.0
    row = 1 # first line should be omitted

    while row < len(data):
        
        cells = data[row].split(',')
        cells[0] = int(cells[0])
        cells[1] = float(cells[1])
        if (len(minPrecipitation) == 0 or
            cells[1] < minPrecipitation[1]):
            minPrecipitation = [cells[0], cells[1]]

        if (len(maxPrecipitation) == 0  or
            cells[1] > maxPrecipitation[1]):
            maxPrecipitation = [cells[0], cells[1]]
            
        averagePrecipitation += cells[1]

        row += 1
        
    print ("min precipitation was", minPrecipitation[1], end='')
    print (" and it occurred in",minPrecipitation[0],)
    
    print ("max precipitation was", maxPrecipitation[1], end='')
    print (" and it occurred in",maxPrecipitation[0])
        
    print ("the average precipitation in last century was",
           averagePrecipitation/(len(data)-1))


    
