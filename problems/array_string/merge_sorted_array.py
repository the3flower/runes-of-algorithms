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
    pass

# Input
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
# Representing the number of elements in nums1 and nums2
m = 3 # nums1
n = 3 # nums2

print(merge_v1(nums1, m, nums2, n))