class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {} 
        # index is count with [[nums1, num2], [nums3]]
        freq = [[] for i in range(len(nums)+1)] 
        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)
        for key, val in countMap.items():
            freq[val].append(key)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                if len(res) == k:
                    break
                else:
                    res.append(freq[i][j]) 
        return res
            
