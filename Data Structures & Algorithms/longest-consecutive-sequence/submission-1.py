class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueSet = set(nums)
        print(uniqueSet)
        longestCount = 0
        for num in nums:
            current = num
            currentMaxCount = 1
            while current + 1 in uniqueSet:
                currentMaxCount += 1
                current += 1
            longestCount = max(currentMaxCount, longestCount)

        return longestCount