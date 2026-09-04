class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            try:
                op = int(op)
                stack.append(op)
            except ValueError:
                if op == "+":
                    stack.append(stack[-1]+stack[-2])
                elif op == "C":
                    stack.pop()
                elif op == "D":
                    stack.append(stack[-1]*2)
                else:
                    return -1
        return sum(stack)
                