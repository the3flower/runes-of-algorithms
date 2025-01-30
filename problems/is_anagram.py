def is_anagram_v1(s, t):
    if len(s) != len(t):
        return False

    s = sorted(s)
    t = sorted(t)

    count = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            count += 1

    if count == len(s):
        return True

    return False


# Input
s = "anagram"
t = "nagaram"

# v1
print(is_anagram_v1(s, t))