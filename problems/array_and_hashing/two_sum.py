# Brute Force
def two_sum_v1(arr, target):
    n = len(arr)

    for i in range(n-1): # n-1 avoid duplicate pair
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    
    return [] # not found

"""
Two sum with Hash

Create hash(dict) for key(complement check):value(index)
- 
- loop for
    - complement = (target) - (current array)
    - if complement is in dict and 

"""
def two_sum_v2(arr, target):
    numMap = {}
    n = len(arr)

    # build hash table
    for i in range(n):
        numMap[arr[i]] = i
        print(numMap)

    # Find the complement
    for i in range(n):
        complement = target - arr[i]
        print(complement)

        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]

    return []  # No solution found

def two_sum_v3(arr, target):
    num_hash = {}

    for i, value in enumerate(arr):
        complement = target - value

        if complement in num_hash:
            return (num_hash[complement], i)

        # add value into hash
        num_hash[value] = i

# Input
arr = [1, 7, 11, 15, 2]
target = 9

print(two_sum_v3(arr, target))
