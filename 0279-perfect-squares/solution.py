from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        
        queue = deque([n])  #存目前還沒歸零的數字
        visited = {n} #避免重複走訪同一個數字
        level = 0
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                cur = queue.popleft()  #從 queue 的最前端取出一個元素，並把它從 queue 移除，賦值給 cur
                j = 1
                while j * j <= cur:
                    next_val = cur - j * j
                    if next_val == 0:
                        return level
                    if next_val not in visited:
                        visited.add(next_val)
                        queue.append(next_val)
                    j += 1
        return level
