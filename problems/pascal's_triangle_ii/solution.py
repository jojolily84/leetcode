class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = []
        for i in range(rowIndex+1):
            row = []
            for j in range(i+1):
                if j == 0:
                    row.append(1)
                elif j == i:
                    row.append(1)
                else:
                    row.append(prev[j-1] + prev[j])
            prev = row
        return prev    