class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            try:
                op = int(op)
                stack.append(op)
            except ValueError:
                if op == "+":
                    r1 = stack.pop()
                    r2 = stack.pop()
                    stack.append(r2)
                    stack.append(r1)
                    stack.append(r1+r2)
                    print(stack)
                elif op == "C":
                    stack.pop()
                elif op == "D":
                    r1 = stack.pop()
                    stack.append(r1)
                    stack.append(r1*2)
                else:
                    return -1
        return sum(stack)
                