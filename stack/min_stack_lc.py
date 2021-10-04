# here the idea is to keep the track of minimum value, push it along with the actual value
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(12)
obj.push(7)
obj.push(19)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)
