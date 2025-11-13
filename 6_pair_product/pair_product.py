''' PAIR PRODUCT 
write a function, pair_product, thata takes in a list and a target product as arguments. The function should  return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique. 

* Be sure to return the indices, not the elements themselves
* There is guaranteed to be one such pair whose product is the target
'''


def pair_product(numbers, target_sum): 
    previous_numbers = {}
    for index, num in enumerate(numbers): 
        complement = target_sum/num
        if complement in previous_numbers: 
            return (previous_numbers[complement], index)
        
        previous_numbers[num]=index


# Test
print(pair_product([4, 7, 9, 2, 5, 1], 5)) # --> (4, 5)
print(pair_product([3, 2, 5, 4, 1], 10))   # --> (1, 2)
print(pair_product([3, 2, 5, 4, 1], 8))    # --> (1, 3)

# Complexity
"""
    time complexity: O(n)
    space complexity: O(n)
"""
