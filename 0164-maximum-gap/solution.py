class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        max_diff = 0
        for i in range(len(nums)-1):
            max_diff = max(max_diff, nums[i+1]-nums[i])
        return max_diff
        """
        n = len(nums)
        if n < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        bucket_size = max(1, math.ceil((max_val - min_val)/(n-1))) # bucket size 至少為 1，避免除以 0
        bucket_count = (max_val - min_val) // bucket_size + 1
        buckets = [None] * bucket_count
        for num in nums:
            idx = (num - min_val) // bucket_size
            if buckets[idx] is None:
                buckets[idx] = [num, num]
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num) #還沒看懂
        max_gap = 0
        prev_max = min_val
        for bucket in buckets:
            if bucket is None:
                continue # 空 bucket，跳過
            max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]
        return max_gap
