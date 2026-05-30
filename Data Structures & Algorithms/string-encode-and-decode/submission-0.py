class Solution:

    def encode(self, strs: List[str]) -> str:
        returnString = ""
        for strVal in strs:
            returnString += f"{len(strVal)}#{strVal}"
        return returnString

    def decode(self, s: str) -> List[str]:
        res = []
        pointer = 0
        while pointer < len(s):
            hashPointer = pointer
            while s[hashPointer] != "#":
                hashPointer += 1
            
            startIndex = hashPointer + 1
            endIndex = startIndex + int(s[pointer:hashPointer])
            res.append(s[startIndex:endIndex])

            pointer = endIndex
        
        return res
        

