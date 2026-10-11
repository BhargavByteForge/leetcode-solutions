class Solution:
    def mostWordsFound(self, arr: list[str]) -> int:
        ans=0
        for j in range(len(arr)):
            s=arr[j]
            temp=1
            for i in range(len(s)):
                ch=s[i]
                if ch==" ":
                    temp=temp+1
            ans=max(ans,temp)
        return ans