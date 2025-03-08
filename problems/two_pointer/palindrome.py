"""
my idea of valid palindrome
    1. should be even number? "No, Focus more on the symmetry rather than the character count."
    2. remove non-alphanumeric number
    3. can read forward and backward

solution 1: (brute force) cleaning, reversal, and comparing
    1. check empty string, if empty = palindrome
    2. clean up input
        2.1 delete non-alphanumeric
        2.2 delete white space
        2.3 make all input(string) to lower case
    3. finding middle of string
    4. swap all string and compare to output

solution 2: two pointer
    1. set two pointer left and right
    2. set left in the first position, and right at the last position
    3. 
"""

# .isalnum() to check alphanumeric
def isPalindrome1(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # Check alphanumeric
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

s1 = "A man, a plan, a canal: Panama" # true
s2 = "race a car" # false
s3 = "asdfdsa" # true

print(isPalindrome1(s1))