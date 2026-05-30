class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = defaultdict(list)
        for strVal in strs:
            count = [0] * 26

            for char in strVal:
                count[ord(char) - ord('a')] += 1
            values[tuple(count)].append(strVal)

        return list(values.values())