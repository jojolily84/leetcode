# getMin() 必須是 O(1)
# 用「空間換時間」：額外維護一個 stack，同步記錄每個時刻的最小值(維護一個輔助結構，讓它跟主結構同步變化。)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []  #每個 index 對應 stack 中該 index 為 top 時的最小值

    def push(self, value: int) -> None:
        # 若 min_stack 是空的，代表這是目前唯一的值，也就是最小值
        if not self.stack:
            current_min = value
        else:
            current_min = min(value, self.min_stack[-1])
        self.stack.append(value)
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
