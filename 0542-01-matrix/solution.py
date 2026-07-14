from collections import deque
"""與其對每個 1 分別找最近的 0（效率差），不如反過來，把所有 0 當作起點同時開始 BFS，第一次走到某個 1 的距離就是答案。
BFS 找最短路徑是常見套路，但這題的關鍵是「多個起點同時擴散」，本質上等同於在原圖多加一個虛擬源點連到所有 0"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        #-1同時扮演兩個角色:未訪問標記 跟 距離的初始佔位值
        dist = [[-1] * n for _ in range(m)]
        queue = deque()
        
        # Step 1: 所有 0 作為 multi-source，一次全部放入 queue
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
                    
        # Step 2: BFS 向外擴散
        directions = [(-1, 0), (1, 0), (0, -1),(0, 1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
        return dist
