class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = nums[0]
        currentSum = 0
        for i in range(len(nums)):
            if currentSum < 0:
                currentSum = 0
            currentSum += nums[i]
            maxVal = max(maxVal, currentSum)
        return maxVal