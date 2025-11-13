'''
    a function that takes 2 strings as arguments and return a boolean (True or False)
    indicating whether or not the strings are anagrams. Anagrams are strings that contain the same
    charaters, but in any order.  
'''

from collections import Counter


def is_anagram(word1, word2):
    return char_count(word1) == char_count(word2)

def is_anagram(s1, s2): 
    return Counter(s1) == Counter(s2)
    
def char_count(s): 
    dict_count={}
    for char in s: 
        if char not in dict_count: 
            dict_count[char] = 0

        dict_count[char] += 1 

    return dict_count


# Test
print(is_anagram('restful', 'setrluf'))         #--> True
print(is_anagram('cats', 'tocs'))               #--> False
print(is_anagram("astronomer", "moonstarer"))   #--> True

# Complexity
'''
    time complexity: O(n)
    space complexity: O(n)
'''

