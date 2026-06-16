class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            #最小值在最大值的右邊，
            if nums[mid] > nums[right]: 
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1 #是唯一安全且不會跳過最小值的操作
        return nums[left]
