class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for key, freq in res.items():
            buckets[freq].append(key)
        result = []
        for i in range(len(buckets) - 1 , 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result