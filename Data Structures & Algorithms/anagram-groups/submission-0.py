class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = {}
        for strVal in strs:
            sortedVal = "".join(sorted(strVal))

            if sortedVal in values:
                values[sortedVal].append(strVal)
            else:
                values[sortedVal] = [strVal]

        return list(values.values())
