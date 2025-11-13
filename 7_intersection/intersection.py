''' INTERSECTION

    Write a function, intersection, that takes in two lists, a, b, as arguments. The function should
    return a new list containing elements that are in both of the 2 lists.

    You may assume that each input list does not contain duplicate elements.
'''


def intersection_v0(list_1, list_2): 
    result = []
    for i in list_1: 
        if i in list_2: 
            result.append(i)
    return result


def intersection_v1(list_1, list_2): 
    set_list_1 = set(list_1)
    result = []
    for num in list_2: 
        if num in set_list_1: 
            result.append(num)
    return result

# Tests
print(intersection_v0([4, 2, 1, 6], [3, 6, 9 ,2, 10])) # --> [2, 6]
print(intersection_v0([4, 2, 6], [4,2])) # --> [2, 4]
print(intersection_v0([4, 2, 1], [1, 2, 4, 6])) # --> [4, 2, 1]
print(intersection_v0([0, 2, 1], [10,11])) # --> []

a = [i for i in range(0,5000)]
b = [i for i in range(0,5000)]
print(intersection_v1(a, b))

# Complexity
'''
* intersection_v0: 
    time complexity: O(n*m)
    space complexity: O(min(n,m))

* intersection_v1: 
    time complexity: O(n+m)
    space complexity: O(n)
'''