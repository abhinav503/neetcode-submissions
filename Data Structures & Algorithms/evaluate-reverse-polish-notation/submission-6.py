import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        if len(tokens) == 1:
            return int(tokens[0])
        currentRes = ""
        while len(tokens) > 1:
            for i,token in enumerate(tokens):
                if token in operator_map:
                    currentRes = operator_map[token](int(tokens[i-2]), int(tokens[i-1]))
                    tokens[i] = currentRes
                    del tokens[i-2:i]
                    break
        return int(currentRes) if currentRes != "" else 0
