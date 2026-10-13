class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        n=len(nums)
        ans=float("-inf")
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    diff=nums[j]-nums[i]
                    ans=max(ans,diff)
        return ans if  ans != float("-inf") else -1
