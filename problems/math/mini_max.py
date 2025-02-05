def mini_max_v1(arr):
    # Write your code here
    new_arr = []
    result = []
    
    for i in range(len(arr)):
        # new_arr = arr This can leading unexpected behavior
        new_arr = arr[:]
        new_arr.pop(i)
        
        sum = 0
        
        for j in new_arr:
            sum += j
            
        result.append(sum)
        
    return min(result), max(result)

def mini_max_v2(arr):
    pass


    
arr = [1, 2, 3, 4, 5]
print(mini_max_v1(arr))