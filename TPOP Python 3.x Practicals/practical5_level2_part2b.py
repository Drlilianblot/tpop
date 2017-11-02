def readDataFile(fileName):
    try:
        dataFile = open(fileName)
    except IOError as err:
        print ('The following error occurred:',err)
        raise   # We don't want to deal with the error here
                # We let the calling function deal with it.
    else:
        data = dataFile.readlines()
        dataRecords = {}
        dataFile.close()
        row = 1 # first line should be ommitted
        while row < len(data):
            
            cells = data[row].split(',')
            if cells[0] in dataRecords:
                raise ValueError() # there should not be duplicate year in the file
            else:
                dataRecords[int(cells[0])] = float(cells[1])

            row += 1
        return dataRecords
    


def collatePrecipitationFile(fileNames,outputFile):
    '''
    Collate the data of all the files where the name is in the list of string
    fileNames and store the collated data in the file whose name is given by
    the parameter outputfile (a string). files that cannot be opened are simply
    ignored. It is assumed that the data in each file is correct and complete,
    e.g. all contains the same years. Note no checking is done regarding the
    validity of the data.
    The data is written as a CSV file.
    
    '''
    listDataRecords = {}    # keys are years, value are list of three floats:
                    # precipitation for Europe, NAmerica, World or whatever the 
                    # files past in parameters
    validListOfFiles = []
    for name in fileNames:
        try:
            dataRecords = readDataFile(name)
        except IOError as err:
            print ('The following error occurred:',err)
        except ValueError as err:
            print ("duplicate year in file", name)
        else:
            validListOfFiles.append(name)
            for item in dataRecords.items():
                if item[0] in listDataRecords:
                    listDataRecords[item[0]].append(item[1])
                else:
                    listDataRecords[item[0]] = [item[1]]

    ## This section of the code deals with writing the collated data to
    ## a text file (.CSV)
    outputF = open(outputFile,'w')
    # write the header of the file, e.g. column names
    outputF.write('Years,')
    outputF.write(','.join(validListOfFiles))
    outputF.write('\n')
    outputF.flush()

    # write the data. item is a tuple containing item[0]: the key (e.g. year)
    # and item[1] the list of values (three in this case) corresponding the
    # precipitation for that particular year.
    for item in sorted(listDataRecords.items()):
        outputF.write(str(item[0]))
        for value in item[1]:
            outputF.write(',')
            outputF.write(str(value))
        outputF.write('\n')
        outputF.flush()

    outputF.close()



##########################################
##      TESTS
#########################################

    
listOfFiles = ['Data/precipitations-europe.txt',
           'Data/precipitations-NAmerica.txt',
           'Data/precipitations-world.txt']

collatePrecipitationFile(listOfFiles, 'Data/collated.txt')
