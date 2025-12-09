
''' Tribonacci

    Write a function tribonacci that takes in a number argument, n. and returns the n-th number of the tribonacci sequence.
    The 0-th and 1-st numbers of the sequence are both 0.
    the 2-nd number of the sequence is 1.

    To generate further numbers of the sequence, calculate the sum of previous three numbers. 
    
    Solve this recursively!!!
'''

def tribonacci(n):
    return _trib(n, {})

def _trib(n, memo): 
    if n in memo: 
        return memo[n]
    if n < 2: 
        return 0 
    if n == 2: 
        return 1
    
    memo[n] =  _trib(n-1, memo) + _trib(n-2, memo) + _trib(n-3, memo)
    return memo[n]



# tests 
print(tribonacci(0))
print(tribonacci(1))
print(tribonacci(2))
print(tribonacci(6))
print(tribonacci(20))
print(tribonacci(37))