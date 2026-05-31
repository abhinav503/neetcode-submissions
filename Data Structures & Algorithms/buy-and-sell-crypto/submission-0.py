class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minPrice = prices[0]
        maxProfitV = 0

        for price in prices:
            minPrice = min(price, minPrice)
            maxProfitV = max(maxProfitV ,price - minPrice)
        
        return maxProfitV