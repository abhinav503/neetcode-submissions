class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        
        sortedMap = dict(sorted(countMap.items(), key=lambda item: item[1], reverse=True))
        return list(sortedMap.keys())[0:k] 