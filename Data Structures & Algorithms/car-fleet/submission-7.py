class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = sorted(zip(position, speed), reverse=True)
        res = 0
        maxTime = 0
        for p,s in paired:
            time = (target - p)/s
            if time > maxTime:
                res += 1
                maxTime = time
        return res

