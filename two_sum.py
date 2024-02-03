def twoSum(nums, target):
    # Create a dictionary to store the indices of elements
    num_indices = {}

    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement needed to achieve the target
        complement = target - num
        print(complement)

        # Check if the complement is already in the dictionary
        if complement in num_indices:
            # If yes, return the indices of the two numbers
            return [num_indices[complement], i]

        # If the complement is not in the dictionary, store the current number and its index
        num_indices[num] = i
        print(num_indices)

    # If no solution is found, return an empty list
    return []

# Example usage:
nums1, target1 = [2, 7, 11, 15], 9
print(twoSum(nums1, target1))  # Output: [0, 1]

nums2, target2 = [3, 2, 4], 6
print(twoSum(nums2, target2))  # Output: [1, 2]

nums3, target3 = [3, 3], 6
print(twoSum(nums3, target3))  # Output: [0, 1]
