class MinStack:
    def __init__(self):
        self.q = deque()
        self.minstack = deque()

    def push(self, val: int) -> None:
        self.q.append(val)
        if len(self.minstack) == 0 or self.getMin() > val:
            self.minstack.append(val)
        else:
            self.minstack.append(self.getMin())
        return

    def pop(self) -> None:
        self.minstack.pop()
        self.q.pop()
        return

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.minstack[-1]