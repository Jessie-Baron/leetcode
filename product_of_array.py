def productExceptSelf(nums):
    n = len(nums)

    # Initialize left and right arrays to store products to the left and right of each element
    left_products = [1] * n
    right_products = [1] * n

    # Calculate products to the left of each element
    left_product = 1
    for i in range(1, n):
        left_product *= nums[i - 1]
        left_products[i] = left_product

    # Calculate products to the right of each element
    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        right_products[i] = right_product

    # Multiply the corresponding elements from left and right arrays to get the final result
    result = [left_products[i] * right_products[i] for i in range(n)]

    return result

# Example usage:
nums1 = [1, 2, 3, 4]
print(productExceptSelf(nums1))
# Output: [24, 12, 8, 6]

nums2 = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums2))
# Output: [0, 0, 9, 0, 0]
