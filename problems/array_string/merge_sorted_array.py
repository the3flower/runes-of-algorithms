# CANNOT do like this, do not modify list when iterate forward
def merge_v1(nums1, m, nums2, n):
    # Clean zeros in array(1)
    # CANNOT do like this, do not modify list when iterate forward
    # for i in range(len(nums1)):
    #     if nums1[i] == 0:
    #         nums1.pop()

    # for i in range(len(nums2)):
    #     if nums2[i] == 0:
    #         nums2.pop()

    # Clean zeros in array(2)
    

    print(nums1)
    print(nums2)

def merge_v2(nums1, m, nums2, n):
    # Set 3 pointers
    # pointer for nums1
    p1 = m-1
    # pointer for nums2
    p2 = n-1
    # pointer for placing element in nums1
    p = m+n-1

    # Merge from the end to the start
    while p2 >= 0: # loop til nums2 merge to nums1
        if p1 >= 0 and nums1[p1] > nums2[p2]: # check **p1 non-negative and nums1[p1] > nums2[p2]
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1

        p -= 1

    print(nums1)

# append and sort ggez
def merge_v3(nums1, m, nums2, n):
    nums1[m:] = nums2 # start from index m to the end, e.g. m = 3 start from the first 0(zero) to replace 0 with nums2
    nums1.sort()

    print(nums1)

# Input
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
# Representing the number of elements in nums1 and nums2
m = 3 # nums1
n = 3 # nums2

print(merge_v3(nums1, m, nums2, n))