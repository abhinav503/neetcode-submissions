class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        i = 0
        pos = {}
        paired = sorted(zip(position, speed), reverse=True)
        while i < len(paired):
            pos[paired[i][0]] = [paired[i][1], ((target-paired[i][0])/paired[i][1])]
            i += 1
        res = []
        for value in list(pos.values()):
            if not res:  
                res.append(value[1])
            else:
                if res[-1] >= value[1]:
                    continue
                else:
                    res.append(value[1])
        return len(res)
