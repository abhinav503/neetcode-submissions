class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for i in s]
        resIdx = 0
        resLen = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > resLen:
                        resIdx  = i
                        resLen = j-i+1
        return s[resIdx : resIdx+resLen]
        

        
        
