import math

def max_value(numbers): 
    '''
    This function finds the maximum number in a list of number
    '''
    maximum = float('-inf')
    for num in numbers: 
        if num > maximum: 
            maximum = num
    return maximum

'''
    time complexity: O(n)
    space complexity: O(1)
'''


numbers = [3, 5, 7,3, 9, 2, 1]
print(max_value(numbers))