class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count1,count0 = 0, 0
        max_count1, max_count0 = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                count1 += 1
                count0 = 0
                max_count1 = max(max_count1, count1)
            else:
                count0 += 1
                count1 = 0
                max_count0 = max(max_count0, count0)
        return max_count1 > max_count0