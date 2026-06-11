class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        bucket_size = max(1, math.ceil((max_val - min_val) / (n - 1))) # bucket size 至少為 1，避免除以 0
        bucket_count = (max_val - min_val) // bucket_size + 1
        buckets = [None] * bucket_count # 每個 bucket 存 [local_min, local_max]，None 代表空的
        
        #bucket 內部最大差距 < bucket_size
        #平均 gap = bucket_size
        #∴ 最大 gap ≥ bucket_size > bucket 內部差距
        
        for num in nums:
            idx = (num - min_val)//bucket_size
            if buckets[idx] is None:
                buckets[idx] = [num, num]
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)
                
        max_gap = 0
        prev_max = min_val
        for bucket in buckets:
            if bucket is None: # 空 bucket，跳過
                continue
            max_gap =max(max_gap, bucket[0] - prev_max) # 這個bucket的min - 上一個bucket的max
            prev_max = bucket[1]
        return max_gap
