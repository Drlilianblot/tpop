def build_largest_int(numbers):
    """
    Function that given a list of non negative integers, arranges them such
    that they form the largest possible number.
    For example, given [50, 2, 1, 9], the largest formed number is 95021.
    """

    numbers_str = []
    for number in numbers:
        numbers_str.append(str(number))

    numbers_str = sorted(numbers_str, reverse=True)
    return "".join(numbers_str)
    
def build_largest_int_brute(numbers):
    """
    Function that given a list of non negative integers, arranges them such
    that they form the largest possible number.
    For example, given [50, 2, 1, 9], the largest formed number is 95021.
    """
    if numbers == []:
        return [""]
    numbers_str = []
    for index in range(len(numbers)):
        remaining_numbers = numbers[0:index]
        if index < len(numbers) - 1:
            remaining_numbers += numbers[index+1:]
        print()
        sub_numbers = build_largest_int_brute(remaining_numbers)
        print(numbers[index], "-->", remaining_numbers,'::',sub_numbers)
        if sub_numbers == []:
            numbers_str.append(str(numbers[index]))
        else:
            for num in sub_numbers:
                numbers_str.append(str(numbers[index])+num)
                
        print(numbers_str)
        
    return numbers_str
    


def gethundred():
    """
    Write a program that outputs all possibilities to put + or - or nothing
    between the numbers 1, 2, ..., 9 (in this order) such that the result is
    always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.
    """
    def recursive(expression, digits):
        result = []
        if digits == []:
            command = "".join(expression)
            try:
                value = eval(command)
            except:
                return []
            
            if value == 100:
                print(command)
                result.append(command)
        else:
            if not expression: # dont start an expression with +1, just 1
                result += recursive(expression[:] + ['-'], digits[:])
                result += recursive(expression[:] + [str(digits[0])], digits[1:])
                
            elif expression and (expression[-1] == '-'
                               or expression[-1] == '+'):
                # don't have multiple successive operators such as 1+--2
                result += recursive(expression[:] + [str(digits[0])], digits[1:])
            else:    
                result += recursive(expression[:] + ['-'], digits[:])
                result += recursive(expression[:] + ['+'], digits[:])
                result += recursive(expression[:] + [str(digits[0])], digits[1:])

        return result

    return recursive([],[1,2,3,4,5,6,7,8,9])
            

# print(gethundred())

print(build_largest_int_brute([50, 2, 1, 9]))
