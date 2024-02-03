
def isAnagram(s, t):
    # Check if lengths are different, if yes, return False
    if len(s) != len(t):
        return False

    # Initialize a dictionary to store character counts
    char_count = {}

    # Iterate through string s and update character counts
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Iterate through string t and update character counts
    for char in t:
        # If character is not in the dictionary, or count becomes zero, return False
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    # If all characters have been matched, return True
    return True

# Example usage:
s1, t1 = "anagram", "nagaram"
print(isAnagram(s1, t1))  # Output: True

s2, t2 = "rat", "car"
print(isAnagram(s2, t2))  # Output: False
