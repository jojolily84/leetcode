class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #return sort(num**2 for num in nums) 直接解 O(n log n)
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        pos = n - 1 #結果陣列從尾端填入
        while left <= right:
            l_sq = nums[left] ** 2
            r_sq = nums[right] ** 2
            if l_sq > r_sq:
                res[pos] = l_sq
                left += 1
            else:
                res[pos] =r_sq
                right -= 1
            pos -= 1
        return res
