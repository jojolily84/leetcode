class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.feasible(nums, mid, k):
                right = mid  # mid 可行，往更小找
            else:
                left = mid +1  # mid 太小，往右移
        return left
    def feasible(self, nums, limit, k):
        count = 1  # 目前用了幾個 subarray
        current =0  # 目前這個 subarray 的累積 sum
        for n in nums:
            if current + n > limit:
                count += 1  # 裝不下，開新的
                current = 0
            current += n  # 把 n 放進目前的 subarray
        return count <= k
