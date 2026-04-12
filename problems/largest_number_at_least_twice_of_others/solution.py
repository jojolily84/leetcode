class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index, m = max(enumerate(nums), key = lambda x : x[1])
        for i, num in enumerate(nums):
            if i == max_index:
                continue
            if m < 2 * num:
                return -1
        return max_index