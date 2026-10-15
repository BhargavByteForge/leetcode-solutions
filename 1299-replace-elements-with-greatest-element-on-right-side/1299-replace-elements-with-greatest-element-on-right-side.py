class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n=len(arr)
        sol=-1
        for i in range(n-1,-1,-1):
            temp=arr[i]
            arr[i]=sol
            sol=max(sol,temp)
        return(arr)
