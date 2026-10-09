class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      d={}
      for z in range(len(nums)):
        if (target-nums[z] not in d):
            d[nums[z]]=z
        else:
            return [z,d[target-nums[z]]]  