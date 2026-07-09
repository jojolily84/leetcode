from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        if start in dead:
            return -1
        if start == target:
            return 0
        visited = set(dead)  #建立一個新的set，複製dead的內容進去
        visited.add(start)
        queue = deque([(start, 0)])  #建立一個 deque，裡面預先放入一個 tuple ("0000", 0)
        while queue:  #只要 queue 裡還有東西，就繼續跑迴圈
            state, steps = queue.popleft()   # state = "0000", steps = 0
            
            for i in range(4):
                digit = int(state[i])
                for delta in (-1, 1):  #轉動 +1 , -1
                    new_digit = (digit + delta) % 10  #wrap around
                    next_state = state[:i] + str(new_digit) + state[i+1:]
                    
                    if next_state == target:
                        return steps + 1
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, steps + 1))
        return -1
