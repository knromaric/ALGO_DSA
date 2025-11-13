"""
    A prime number is a number that is only divisible by 1 and itself. 

    here we write a function "is_prime" that takes a number as argument 
    and return a boolean.
         True : the given number is Prime
         False: the givent number is NOT Prime
"""

from  math import sqrt, floor

def is_prime(num): 
    if num < 2: 
        return False
    
    for i in range(2, floor(int(sqrt(num)))+1): 
        if num % i == 0: 
            return False
    return True

# Tests
print(is_prime(64)) # --> False
print(is_prime(13)) # --> True
print(is_prime(5))  # --> True
print(is_prime(21)) # --> False

# Complexity
'''
    time complexity: O(sqrt(n))
    space complexity: O(1)
'''