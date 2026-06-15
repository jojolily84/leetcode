class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # mid 在較大的那半段，minimum 必在右邊
                left = mid + 1
            else:  # mid 可能就是 minimum，或在左半段
                right = mid
        return nums[left]
