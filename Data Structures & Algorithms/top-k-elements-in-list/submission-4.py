class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        res = dict(sorted(res.items(), key=lambda item: item[1]))
        return list(res.keys())[-k:]
