class MyQueue:
    
    #用兩個 stack 模擬 queue，核心概念是利用第二個 stack 做「反轉」
    #把 in-stack 的元素倒進 out-stack，順序就會從 LIFO 反轉成 FIFO。
    #關鍵在於 lazy transfer：只有當 out-stack 空了才需要搬移，這樣才能達到 amortized O(1)。

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._transfer()  # 先確保 out_stack 是「可用」狀態
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer()  # 先確保 out_stack 是「可用」狀態
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
        
    def _transfer(self) -> None:
        # 只有 out_stack 空了才搬，避免破壞已排好的順序
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
