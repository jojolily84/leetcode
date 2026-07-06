class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #defaultdict():建構時傳入一個factory function，當存取不存在的key時，會自動呼叫這個factory產生預設值並放進去
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)  #key:(r//3, c//3)
        for r in range(9):
            for c in range(9):
                #board[r][c]是Python對nested list(2D list)的標準indexing語法，只要board存在，board[r][c]就能直接用。
                val = board[r][c]
                if val == '.':
                    continue
                box_key = (r // 3, c // 3)
                
                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)
        return True
