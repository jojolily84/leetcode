class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        result = []
        for d in range(m + n - 1):
            if d % 2 == 0: #向上
                row = min(d, m - 1) #起點在左邊界 col=0
                col = d - row
                while 0 <= row and col < n:  #對角整列
                    result.append(mat[row][col])
                    row -= 1
                    col += 1
            else: #向下
                col = min(d, n - 1) #起點在上邊界 row=0
                row = d - col
                while 0<= col and row < m:
                    result.append(mat[row][col])
                    row += 1
                    col -= 1
        return result