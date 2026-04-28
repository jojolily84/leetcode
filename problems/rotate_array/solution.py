class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        x = k % n
        new_nums = nums[n-x:n] + nums[:n-x]
        nums[:] = new_nums