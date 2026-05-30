class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}

        for i,val in enumerate(nums):
            remaining[val] = i;

        for i,val in enumerate(nums):
            if target - val in remaining and  (remaining[target-val] != i):
                return [i, remaining[target-val]]

        return [0,1]