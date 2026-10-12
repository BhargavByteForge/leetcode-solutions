class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mx=0
        mn=prices[0]
        for price in prices[1:]:
            mx=(max(mx,price-mn))
            mn=min(mn,price)
        return mx

