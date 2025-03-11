def contain_duplicate(arr):
    if len(arr) != len(set(arr)):
        return False
    
    return True

arr = [1, 2, 3, 4, 1]

print(contain_duplicate(arr))