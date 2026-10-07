class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s=1
        for p in range(2,int(num**0.5)+1):
            if num%p==0:
                s+=p
                if p!=num//p:
                    s+=num//p 
        return s==num and s!=1
