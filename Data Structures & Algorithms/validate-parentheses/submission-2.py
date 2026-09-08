class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in ')]}' :
                if len(stack) == 0:
                    return False
                r = stack.pop()
                if r == '(' and c == ')':
                    continue
                elif r == '[' and c == ']':
                    continue
                elif r == '{' and c == '}':
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        return True