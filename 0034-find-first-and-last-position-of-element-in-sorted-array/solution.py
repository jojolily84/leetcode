class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        #找 leftmost target（第一個出現位置）
        def find_left(nums, target):
            left, right = 0, len(nums)-1
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            # 結束時 left, right 相鄰，先檢查 left 再 right
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            return -1
        
        def find_right(nums, target):
            left, right = 0, len(nums)-1
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid
            # 先檢查 right 再 left
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left
            return -1
        return [find_left(nums, target), find_right(nums, target)]
