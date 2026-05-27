class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #初始化[set(),set(),set(),set(),set(),set(),set(),set(),set()]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c)) #蒐集空格的位置
                else:
                    ch = board[r][c]  #紀錄有數字的位置跟資料
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[(r // 3) * 3 + (c // 3)].add(ch)
        def backtrack(i):
            if i == len(empties):  #表示前面i-1個資料都完成了
                return True
            r, c = empties[i]
            b=(r // 3) * 3 + (c // 3)
            for ch in '123456789':
                #已經有的數字，continue下一步
                if((ch in rows[r]) or
                   (ch in cols[c]) or
                   (ch in boxes[b])
                ):
                    continue
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[b].add(ch)
                if backtrack(i+1):
                    return True
                board[r][c] = '.'
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[b].remove(ch)
            return False
        backtrack(0)