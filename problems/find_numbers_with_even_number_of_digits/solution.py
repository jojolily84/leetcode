class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        length=0
        for num in nums:
            if len(str(num)) % 2 == 0:
                length += 1
        return length          