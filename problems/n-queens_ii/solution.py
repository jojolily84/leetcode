class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag1 = set() #row-col
        diag2 = set() #row+col
        self.count = 0
        def backtrack(row):
            if row == n:   #完成0~n-1
                self.count += 1
                return
            for col in range(n):
                if (col in cols or 
                    (row - col) in diag1 or 
                    (row + col) in diag2
                ): #會衝突的判斷條件
                    continue
                    #放queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                    
                backtrack(row + 1) #下一列
                    
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
        backtrack(0)
        return self.count