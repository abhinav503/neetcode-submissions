class Solution:
    def isPalindrome(self, s: str) -> bool:
        formattedString = ""

        for char in s:
            if re.match(r"^[a-zA-Z0-9]$", char):
                formattedString += char.lower()
        
        start = 0
        end = len(formattedString) - 1
        while start < end:
            if formattedString[start] == formattedString[end]:
                start += 1
                end -= 1
                continue
            else: 
                return False
        return True

