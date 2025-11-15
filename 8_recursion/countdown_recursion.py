'''Countdown Recursion
    Write a function that implement a countdown, that takes a number, then countdown and display result
    at each step.
'''

def countdown(n): 
    if n == 0: 
        return 
    print('Entering', n)
    countdown(n-1)
    print('return',n)


# Tests 
countdown(5)