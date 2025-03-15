def three_sum(nums):
    num_hash = {}

    pass

nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
"""
return x + y + z = 0

x + y = -z

solution 1
    - create hash by dict
    - loop for pick two values
        - if complement of two sum values is in hash, return complement and two values
            x = 2
            y = -1
            z = -1

            complement = x + y + 0

            -1 = 2 + (-1) + 0
        - if not add to hash
"""

print(three_sum(nums))