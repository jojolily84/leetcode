class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        result = []
        for i in range(n):
            row = []
            for j in range(i+1):
                if j == 0:
                    row.append(1)
                elif j == i+1-1:
                    row.append(1)
                else:
                    row.append(result[i-1][j-1]+result[i-1][j])
            result.append(row)
        return result            