class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left=0
        right=0
        while right<(len(nums)):
            if (nums[left]!=0 and nums[right]!=0):
                left+=1
                right+=1
            elif (nums[left]==0 and nums[right]!=0):
                nums[left],nums[right]=nums[right],nums[left]
                right+=1
                left+=1
            else:
                right+=1


    