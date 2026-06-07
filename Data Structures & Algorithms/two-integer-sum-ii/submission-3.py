class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r:
            if target == numbers[l] + numbers[r]:
                return [min(l,r)+1, max(l,r)+1]
            elif target > numbers[l] + numbers[r]:
                l += 1
            elif target < numbers[l] + numbers[r]:
                r -= 1
        return []
