import heapq
from collections import Counter

def topKFrequent(nums, k):
    # Count the frequency of each element using Counter
    frequency_counter = Counter(nums)

    # Create a min heap (priority queue)
    heap = []

    # Iterate through the elements in the frequency counter
    for num, freq in frequency_counter.items():
        # Push a tuple (frequency, element) onto the heap
        heapq.heappush(heap, (freq, num))

        print(heap)
        # If the size of the heap exceeds k, pop the smallest element
        if len(heap) > k:
            heapq.heappop(heap)
    # The heap now contains the k most frequent elements
    result = [ele for freq, ele in heap]

    return result

# Example usage:
nums1, k1 = [1, 1, 1, 2, 2, 3], 2
print(topKFrequent(nums1, k1))
# Output: [1, 2]

nums2, k2 = [1], 1
print(topKFrequent(nums2, k2))
# Output: [1]
