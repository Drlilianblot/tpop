'''
Created on 5 Nov 2015

@author: lilian
'''
def fibonacciSequence(size):
    sequence= [1, 1]
    for i in range(2, size):
        sequence.append(sequence[i-2] + sequence[i-1])
        
    return sequence

print ("The 100th value in the Fibonacci sequence is:", fibonacciSequence(100)[-1])