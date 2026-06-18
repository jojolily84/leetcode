class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def count_pairs(mid: int) -> int:  #計算 distance <= mid 的 pair 數量
            count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left #count = count + (right - left)
            return count
        lo, hi = 0,nums[-1] - nums[0] # distance 的可能範圍
        while lo < hi:
            mid = (lo + hi) // 2
            if count_pairs(mid) >= k:
                hi = mid  # 可能是答案，往左縮
            else:
                lo = mid + 1
        return lo
