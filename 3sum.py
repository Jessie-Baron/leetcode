def three_sum(nums):
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates for i

        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result

# Example usage:
nums1 = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums1))  # Output: [[-1, -1, 2], [-1, 0, 1]]

nums2 = [0, 1, 1]
print(three_sum(nums2))  # Output: []

nums3 = [0, 0, 0]
print(three_sum(nums3))  # Output: [[0, 0, 0]]
