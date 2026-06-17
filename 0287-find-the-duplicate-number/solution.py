class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo, hi = 1, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            count = sum(1 for x in nums if x <= mid)
            if count > mid:
                hi = mid
            else:
                lo = mid + 1
        return lo
