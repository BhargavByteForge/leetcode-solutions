class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while (left<=right):
            mp=(left+right)//2
            if nums[mp]==target:
                return mp
            elif nums[mp]>target:
                right =mp-1
            else:
                left=mp+1
        return -1