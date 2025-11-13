
""" PAIR SUM

    Write a function pair_sum, that takes in a list and target sum as arguments. The function should 
    return a tuple containing a pair of indice whose elements sum to the given target. The indices 
    returned must be unique.

    * Besure to return the indices, not the elements themselves
    * There is guaranteed to be one such pair that sums to the target
"""


## brute force method 
def pair_sum_v0(numbs, target_sum): 
    for i in range(0, len(numbs)): 
        for j in range(i+1, len(numbs)): 
            if numbs[i] + numbs[j] == target_sum: 
                return (i, j)
            

def pair_sum_v1(numbs, target_sum): 
    previous_numbers = {}
    for index, num in enumerate(numbs): 
        complement = target_sum - num
        if complement in previous_numbers: 
            return (previous_numbers[complement], index)
         
        previous_numbers[num] = index 
    

# Test pair_sum_v0
print(pair_sum_v0([3, 2, 5, 4, 1], 8)) # --> (0,2)
print(pair_sum_v0([4, 7, 9, 2, 5, 1], 5)) # --> (0,5)
print(pair_sum_v0([4, 7, 9, 2, 5, 1], 3)) # --> (3,5)

# Test pair_sum_v1
print(pair_sum_v1([3, 2, 5, 4, 1], 8)) # --> (0,2)
print(pair_sum_v1([4, 7, 9, 2, 5, 1], 5)) # --> (0,5)
print(pair_sum_v1([4, 7, 9, 2, 5, 1], 3)) # --> (3,5)

# Complexity
'''
    * pair_sum_v0
        time complexity: O(n^2)
        space complexity: O(1)

    * pair_sum_v1
        time complexity: O(n)
        space complexity: O(n)
'''




