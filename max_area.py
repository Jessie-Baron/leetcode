def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        current_area = 0
        current_distance = 0

        left, right = 0, len(height) - 1

        for i in range(len(height) - 1):

            current_distance = right - left

            if height[left] >= height[right]:

                if current_area < current_distance * height[right]:

                    current_area = current_distance * height[right]
                    right -= 1

                else:

                    right -= 1

            elif height[right] >= height[left]:

                 if current_area < current_distance * height[left]:
                    current_area = current_distance * height[left]

                    left += 1
                 else:
                    left += 1

        return current_area
