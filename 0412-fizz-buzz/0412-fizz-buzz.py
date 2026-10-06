class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        solu=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                solu.append("FizzBuzz")
            elif i%3==0:
                solu.append("Fizz")
            elif i%5==0:
                solu.append("Buzz")
            else:
                solu.append(str(i))
        return solu