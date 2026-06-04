class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for char in s:
            if char in set({"[", "{", "("}):
                stack.append(char)
            else:
                if len(stack) > 0:
                    if char == "]" and stack[-1] == "[":
                        stack.pop()
                    elif char == "}" and stack[-1] == "{":
                        stack.pop()
                    elif char == ")" and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
        if len(stack) > 0:
            return False  
        return True