class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        if len(nums) == 0:
            return []
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        sortedPairs = sorted(frequency.items(), key=lambda x: x[1])
        sortedMap = dict(sortedPairs)
        keysList = list(sortedMap.keys())

        return keysList[-k:]