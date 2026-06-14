class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = sum(x for x in nums if x < 10)
        double = sum (x for x in nums if x >=10)
        return single != double
