'''
Created on 3 Nov 2016

@author: Lilian
'''

########### EXERCISE 1 ###################

# a_word = "a short string"
# output_file = open("exo1.txt", 'w')
# output_file.write(a_word)
# output_file.close()

########### EXERCISE 2 ###################

def saveListToFile(sentences, filename):
    with open(filename, 'w') as output_file:
        for aSentence in sentences:
            output_file.write(aSentence + '\n')
            

########### EXERCISE 3 ###################

def saveToLog(entry, logfile):
    with open(logfile, 'a') as logs:
        logs.write(entry)
        logs.write('\n')
     
        
########### EXERCISE 4 ###################

# with open('sentences.txt', 'r') as input_file:
#     for line in input_file:
#         print(line.upper())


########### EXERCISE 5 ###################

def toUpperCase(input_file, output_file):
    data_in = []    
    with open(input_file, 'r') as in_file:
        for line in in_file:
            data_in.append(line)
        
    with open(output_file, 'w') as out_file:
        for data in data_in:
            out_file.write(data.upper())
    

########### EXERCISE 6 ###################
def sumNumbers(entry):
    total = 0
    numbers = entry.split()
    for number in numbers:
        total += int(number)
        
    return total
        
def sumFromFile(filename):
    total = 0
    with open(filename, 'r') as input_file:
        for line in input_file:
            total += sumNumbers(line)
            
    return total
                

################## TESTS ################################
# saveListToFile(["line 1", "line 2", "line 3"], "sentences.txt")
# saveToLog("line 4", "sentences.txt")
# saveToLog("line 5", "sentences.txt")
        
# toUpperCase("sentences.txt", "upper.txt")
# print("sum of 1 2 3 4 is 10?", sumNumbers("1 2 3 4") == 10)
# print("sum of '   ' should be 0?", sumNumbers("   ") == 0)
# 
# print("sum of element in numbers.txt is 100", sumFromFile("numbers.txt") == 100)

