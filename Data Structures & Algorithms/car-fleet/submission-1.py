class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = sorted(zip(position, speed), reverse=True)
        res = []
        for pos,spd in paired:
            time = ((target-pos)/spd)
            if not res:  
                res.append(time)
            else:
                if res[-1] >= time:
                    continue
                else:
                    res.append(time)
        return len(res)
