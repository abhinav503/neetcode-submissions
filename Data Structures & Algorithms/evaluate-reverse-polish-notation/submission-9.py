import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }
        stack = []
        for token in tokens:
            if token not in operator_map:
                stack.append(int(token))
            else:
                e2 = stack.pop()
                e1 = stack.pop()
                stack.append(operator_map[token](e1, e2))
        return int(stack[0])
