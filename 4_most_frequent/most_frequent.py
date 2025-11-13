
'''
    Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent
    character of the string. If there are ties, return the character that appears earlier in the string. 
    You can assume that the input string is non-empty.
'''

from math import inf


def most_frequent_letter(s): 
    count = char_count(s)
    most_occ = None
    for char in s: 
        if most_occ is None or count[char] > count[most_occ]: 
            most_occ= char

    return most_occ

def char_count(s): 
    dict_count={}
    for char in s: 
        if char not in dict_count: 
            dict_count[char] = 0
        dict_count[char] += 1 
    return dict_count


# Test
print(most_frequent_letter('potatoe'))   # --> 'o'
print(most_frequent_letter('bookeeper')) # --> 'e'
print(most_frequent_letter('david'))     # --> 'd'
print(most_frequent_letter('abby'))      # --> 'b'


# Complexity
'''
    time complexity: O(n)
    space complexity: O(n)
'''