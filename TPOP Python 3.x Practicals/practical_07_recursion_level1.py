#######################################################
##
##  Question 2
##
#######################################################

def is_power(a,b):
    if b == 0:
        return a == 1 or a == 0
    if (a == 1): # the order of the if-elif and else is very important
                # if you change it, it will not return the right result
        return True
    elif (b == 1):
        return False # as a != 1 a cannot be a power of b
    elif (a%b != 0):
        return False
    else:
        # A common error is to forget to use return. Note, as opposed
        # to n! this is what we call a tail recursion, that could be
        # optimised by some language compiler which removes the
        # recursion.
        return is_power(a/b, b)


#######################################################
##
##  Question 3
##
#######################################################



##RECURSIVE
    
def fib_rec(n):
    if (n == 0):   #base case
        return 0
    elif (n == 1): #base case
        return 1
    else:          #general case
        # again we need to use the return statement. Even though it is
        # the last statement of the recursive function, it is not a 
        # tail recursion. We need to go back up the recursive stack to
        # do the addition, therefore it is not a tail recursion
        return fib_rec(n-1) + fib_rec(n-2)



#ITERATIVE
        
def fib_iter(n):
    if (n == 0):   #base case
        return 0
    elif (n == 1): #base case
        return 1
    else:          #general case
        
        prev_1 = 1 #fib(1) and then fib(n-1)
        prev_2 = 0 #fib(0) and then fib(n-2)
        for i in range(2,n):
            fib = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = fib
        return prev_1 + prev_2

#test with fib_rec(5), fib_rec(10), and fib_rec(30)


