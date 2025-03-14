def group_anagrams(strs):
    bag = {}
    result = []

    for i, value in enumerate(strs):
        if value in strs:
            print(value)

        strs[i] = 0

    pass

    # hash for 

strs = ["eat","tea","tan","ate","nat","bat"]

print(group_anagrams(strs))