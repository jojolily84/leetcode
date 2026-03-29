class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        k = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                k += 1
        return k