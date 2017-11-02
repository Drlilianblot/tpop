dataRecords = {}    # keys are years, value are list of three floats:
                    # precipitation for Europe, NAmerica, World
listOfFiles = ['precipitations-europe.txt',
               'precipitations-NAmerica.txt',
               'precipitations-world.txt']
validListOfFiles = []

for fileName in listOfFiles:
    try:
        dataFile = open(fileName)
    except IOError as err:
        print ('The following error occurred:',err)
    else:
        validListOfFiles.append(fileName)
        data = dataFile.readlines()
        dataFile.close()
        row = 1 # first line should be ommitted
        while row < len(data):
            
            cells = data[row].split(',')

            # convert each cell to its appropriate type rather than keeping
            # all cells as string
            cells[0] = int(cells[0])
            cells[1] = float(cells[1])
            if cells[0] in dataRecords:
                dataRecords[cells[0]].append(cells[1])
            else:
                # must create a list containing a single element
                dataRecords[cells[0]] = [cells[1]]

            row += 1


## This section of the code deals with writing the collated data to
## a text file (.CSV)
try:
    outputFile = open('collatedFiles.txt','w')
except IOError as err:
    print ('The following error occurred:',err)
else:
    # write the header of the file, e.g. column names
    outputFile.write('Years,')
    outputFile.write(','.join(validListOfFiles))
    outputFile.write('\n')
    outputFile.flush()

    # write the data. item is a tuple containing item[0]: the key (e.g. year)
    # and item[1] the list of values (three in this case) corresponding the
    # precipitation for that particular year.
    for item in sorted(dataRecords.items()):
        outputFile.write(str(item[0]))
        for value in item[1]:
            outputFile.write(',')
            outputFile.write(str(value))
        outputFile.write('\n')
        outputFile.flush()

    outputFile.close()

