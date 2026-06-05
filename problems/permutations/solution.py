class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = set()
        def backtrack():
            if len(path) == len(nums):
                result.append(path[:]) #要copy
                return
            for num in nums:
                if num not in used:
                    path.append(num)
                    used.add(num)
                    backtrack()
                    path.pop()
                    used.remove(num)
        backtrack()
        return result