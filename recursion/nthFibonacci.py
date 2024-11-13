#!/usr/bin/env python3


# Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, ... n = (n-1) + (n-2)
# fib(n) = fib(n-1) + fib(n+2) for n>2

# naive way of solving is

def getNthFib(n):
    if (n ==1):
        return 0
    if(n ==2):
        return 1
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)
# It's bad because we are recalculating and we have duplications! 
# T: O(2^n) exponential complexity, S: O(n) we are using stack so we are using memory! we call stack

# memoization (caching) solution:
# T: O(n) S: O(n)
# Memoization helps store previously computed values, making the recursive solution more efficient by avoiding redundant calculations.

def getNthFib2(n, memoize={}):
    # base case
    if n <= 1:
        return n  # bcs for n = 0 and n = 1 the nth fib is the same, so 0 and 1 respectively
    
    # check if it's already in memoize
    if n not in memoize:
        memoize[n] = getNthFib2(n - 1, memoize) + getNthFib2(n - 2, memoize)
    return memoize[n]


n = 4
print(f"The {n}th fib number is {getNthFib2(n)}")

