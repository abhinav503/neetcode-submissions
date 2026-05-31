class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        left = 0
        right = 1
        maxProfitV = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                maxProfitV = max(maxProfitV, prices[right] - prices[left])
            else:
                left = right
            right += 1
        
        return maxProfitV