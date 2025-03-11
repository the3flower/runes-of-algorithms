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

    for char1, char2 in zip(s1, s2):
        count[ord(char1) - ord('a')] += 1  # Increment count for s1
        count[ord(char2) - ord('a')] -= 1  # Decrement count for s2
    
    # zip() 
    # ord() subtract to ASCII
    
    return all(c == 0 for c in count)  # If all counts are zero, it's an anagram


s = "anagram"
t = "nagaram"

print(valid_anagram(s, t))