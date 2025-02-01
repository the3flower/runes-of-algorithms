# Brute Force
def two_sum_v1(arr, target):
    n = len(arr)

    for i in range(n-1): # n-1 avoid duplicate pair
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    
    return [] # not found

def two_sum_v2(arr, target):
    numMap = {}
    n = len(arr)

    # build hash table
    for i in range(n):
        numMap[arr[i]] = i

    
    # Find the complement
    for i in range(n):
        complement = target - arr[i]

        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]

    return []  # No solution found

# Input
arr = [2,7,11,15]
target = 9
print(two_sum_v2(arr, target))
