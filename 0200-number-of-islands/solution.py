class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r: int, c: int) -> None:
            # 邊界條件：出界或是水/已訪問
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return   #停止迴圈
            grid[r][c] = '0' #標記成'0',淹沒
            # 往四個方向擴散, 遞迴呼叫確認有沒有1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)  #四個方向都是0時才會再確認下一個位置
        return count
