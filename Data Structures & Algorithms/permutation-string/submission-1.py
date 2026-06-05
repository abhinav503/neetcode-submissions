class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1List = [0] * 26
        s2List = [0] * 26

        for i in range(len(s1)):
            s1List[ord(s1[i]) - ord('a')] += 1 
            s2List[ord(s2[i]) - ord('a')] += 1
        
        if s1List == s2List:
            return True
        
        for r in range(len1, len2):
            s2List[ord(s2[r]) - ord('a')] += 1
            s2List[ord(s2[r-len1]) - ord('a')] -= 1
            if s1List == s2List:
                return True
        return False