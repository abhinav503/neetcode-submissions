class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costLen = len(cost)
        costofItoReachEnd = [0] * (costLen + 1)
        print(costofItoReachEnd)
        costofItoReachEnd[costLen - 1] = cost[costLen - 1]
        costofItoReachEnd[costLen - 2] = cost[costLen - 2]
        print(costofItoReachEnd)
        i = costLen - 3 if costLen >= 3 else -1
        while i >= 0:
            costofItoReachEnd[i] = cost[i] + min(costofItoReachEnd[i + 1], costofItoReachEnd[i + 2])
            i -= 1
        print(costofItoReachEnd)
        return min(costofItoReachEnd[0], costofItoReachEnd[1])
