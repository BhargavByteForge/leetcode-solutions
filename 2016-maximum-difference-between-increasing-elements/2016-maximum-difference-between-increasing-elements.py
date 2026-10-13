class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        n = len(nums)
        ans = -1
        low = nums[0]

        for j in range(1, n):
            if nums[j] > low:
                diff = nums[j] - low
                ans = max(ans, diff)

            low = min(low, nums[j])

        return ans