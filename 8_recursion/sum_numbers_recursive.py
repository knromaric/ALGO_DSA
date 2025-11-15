''' SUM NUMBERS RECURSIVE 
    write a function sumNumbersRecursive that takes in an array of number and returns the sum of all the 
    numbers in the array. All elements will be integers. Solve this recursively

'''



def sum_recursive(numbers): 
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])



    
# Tests
print(sum_recursive([5, 2, 9, 10])) # --> 26
print(sum_recursive([1, -1, 1, -1, 1, -1, 1])) # --> 1


# Complexity
'''
    Time complexity: O(n^2)
    Space complexity: O(n^2)
'''