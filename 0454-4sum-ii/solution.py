from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Step 1: 記錄 nums1 + nums2 所有可能的 sum 及其出現次數
        sum_ab = defaultdict(int)
        for a in nums1:
            for b in nums2:
                sum_ab[a + b] += 1
        # Step 2: 對 nums3 + nums4 的每個 sum，查詢是否有相反數存在於 sum_ab
        count = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                count += sum_ab[target]
        return count
