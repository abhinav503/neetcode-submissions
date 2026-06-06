class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in temperatures]
        stack = []
        for i,temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                t, index = stack.pop()
                res[index] = i - index 
            stack.append((temperature, i))
        return res
                
            
            