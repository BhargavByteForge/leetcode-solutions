class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            width = r - l
            volume = width * min(height[l], height[r])

            max_area = max(max_area, volume)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area