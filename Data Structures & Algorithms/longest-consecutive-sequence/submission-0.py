class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueSet = set(nums)
        longestStreak = 0
        for num in nums:
            if (num - 1) not in uniqueSet:
                currentNumber = num
                currentStreak = 1

                while currentNumber + 1 in uniqueSet:
                    currentNumber += 1
                    currentStreak += 1

                longestStreak = max(longestStreak,currentStreak)
        return longestStreak 


