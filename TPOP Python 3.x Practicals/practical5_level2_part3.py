# IN THIS MODEL ANSWER, WE ARE USING A SCRIPT, TRY TO TRANSFORM THE SCRIPT
# INTO ONE OR MORE FUNCTION. DISCUSS WITH ONE OF YOUR PEER YOUR SOLUTION,
# ESPECIALLY HOW MANY FUNCTIONS WOULD YOU USE, WHAT EACH FUNCTION SHOULD DO,
# WHAT ARE THE PARAMETERS AND RETURNED VALUES IF ANY.
#
# ANOTHER IMPROVEMENT IS TO WRITE THE DATA LIKE 971.4000000000001 AS 971.4. 
# SEARCH HOW TO FORMAT A STRING BEFORE WRITING THE STRING INTO A FILE.

##########  READING THE DATA FROM FILE ###########

dataFile = open('Data/aberporth_meteorological_data.txt')
data = dataFile.readlines()
dataFile.close()

row = 2 # data starts at row 2 (third row)
yearRecord = {} #keys are years, values are the list of attribute [frost, rain, sunshine]

while row < len(data):
    
    cells = data[row].split(',')
    if cells[0] in yearRecord:
        record = yearRecord.get(cells[0])
        for index in range(4, len(cells)): # 4 as the data we are interested in is in the 5th-7th columns
            record[index - 4] += float(cells[index]) # -4 is the offset for the indices
    else:
        record = []
        for index in range(4, len(cells)):
            record.append(float(cells[index]))

        yearRecord[cells[0]] = record

    row += 1


###### WRITING THE SUMMARY FILE ########
summaryDataFile = open('Data/aberporth_meteorological_data_summary.txt','w')

summaryDataFile.write(data[0])
cells = data[1].split(',')
cells = [cells[0]] + cells[4:] # append the header of each column
summaryDataFile.write(','.join(cells))
summaryDataFile.flush()

for item in sorted(yearRecord.items()):
    line = item[0]
    for value in item[1]:
        line += ',' +str(value)
            
    summaryDataFile.write(line)
    summaryDataFile.write('\n')
    summaryDataFile.flush()


summaryDataFile.close()

