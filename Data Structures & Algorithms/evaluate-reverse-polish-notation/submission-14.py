import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operatorsMap = [
            "+",
            "-",
            "*",
            "/",
        ]
        res = 0
        for token in tokens:
            if token not in operatorsMap:
                stack.append(int(token))
            else:
                i1 = stack.pop()
                i2 = stack.pop()
                if token == "+":
                    res = i1 + i2
                elif token == "-":
                    res = i2 - i1
                elif token == "*":
                    res = i1 * i2
                else:
                    res = int(float(i2)/i1)
                stack.append(res)
        return stack[0]
