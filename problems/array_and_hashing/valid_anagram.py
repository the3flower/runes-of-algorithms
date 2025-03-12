def is_anagram(s, t):
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

def valid_anagram(s1, s2):
    """Checks if two strings are anagrams using character frequency count."""
    if len(s1) != len(s2):
        return False  # Anagrams must have the same length
    
    count = [0] * 26  # Array to store character counts (for lowercase letters)

    for char in s:
        count[ord(char) - ord('a')] += 1

    for char in t:
        if count[ord(char) - ord('a')] == 0:
            return False
        
        count[ord(char) - ord('a')] -= 1

    return True


s = "anagram"
t = "nagaram"

print(valid_anagram(s, t))