class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        temp=n//2
        return nums[temp]