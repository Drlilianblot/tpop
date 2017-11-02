'''
Created on 20 Jan 2015

@author: Lilian Blot
'''

pattern1 = ['-----','.....','-----', '.....', '-----']
pattern2 = ['l.l.l','l.l.l','l.l.l', 'l.l.l', 'l.l.l']

def create_row(size, first_pattern, second_pattern):
    output = ''
    for j in xrange(len(first_pattern)):
        output += '    '
        for i in xrange(size):
            if i%2 == 0:
                output += first_pattern[j]
            else:
                output += second_pattern[j]
        
        output += '\n'
        
    return output

def create_board(size, pattern1, pattern2):
    output = ''
    for i in xrange(size):
        if i%2 == 0:
            output += create_row(size, pattern1, pattern2)
        else:
            output += create_row(size, pattern2, pattern1)
    
    return output


print 
print 
print
print create_board(2, pattern1, pattern2)
print
print
print create_board(3, pattern1, pattern2)
print
print
print create_board(4, pattern1, pattern2)
print 
print 
print

# print create_row(4, pattern1, pattern2),
# print create_row(4, pattern2, pattern1),
# print create_row(4, pattern1, pattern2),
# print create_row(4, pattern2, pattern1)
# print create_row(3, pattern1, pattern2),
# print create_row(3, pattern2, pattern1),
# print create_row(3, pattern1, pattern2)

                