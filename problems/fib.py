"""
Fibonacci sequence
    
    Formula:
        f(n) = f(n-1) + f(n-2)

    * f(0) = 0
      f(1) = 1
"""

def fib_1(n):
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fib_1(n-1) + fib_1(n-2)

def fib_brute(n):
    """Computes Fibonacci using simple recursion (brute force)."""
    if n <= 1:
        return n  # Base case
    return fib_brute(n - 1) + fib_brute(n - 2)  # Recursive case

def fib_memo(n, memo={}):
    """Computes Fibonacci using recursion with memoization (dynamic programming)."""
    if n in memo:
        return memo[n]  # Return stored value if already computed
    if n <= 1:
        return n  # Base case
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)  # Store computed value
    return memo[n]

n = 9
fib_nums = [
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
    6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040,
    1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986,
    102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903
]

print(fib_1(n))