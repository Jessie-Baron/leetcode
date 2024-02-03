def groupAnagrams(strs):
    # Create a dictionary to store groups of anagrams
    anagram_groups = {}

    # Iterate through each string in the input array
    for word in strs:
        # Sort the characters of the word to create a unique key for anagrams
        sorted_word = ''.join(sorted(word))

        # Check if the sorted word is already a key in the dictionary
        if sorted_word in anagram_groups:
            # If yes, append the current word to the existing group
            anagram_groups[sorted_word].append(word)
        else:
            # If no, create a new group with the sorted word as the key
            anagram_groups[sorted_word] = [word]

    # Return the values (lists of anagrams) from the dictionary
    return list(anagram_groups.values())

# Example usage:
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs1))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

strs2 = [""]
print(groupAnagrams(strs2))
# Output: [['']]

strs3 = ["a"]
print(groupAnagrams(strs3))
# Output: [['a']]
