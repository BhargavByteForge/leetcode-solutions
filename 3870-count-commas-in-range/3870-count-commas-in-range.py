class Solution:
    def countCommas(self, n: int) -> int:
        count=0
        if len(str(n))>3:
            count=count+(n-999)
        return count 
