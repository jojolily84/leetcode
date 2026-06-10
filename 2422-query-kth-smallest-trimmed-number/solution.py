class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        answer = []
        for k, trim in queries:
            trimmed = [(nums[i][-trim:], i) for i in range(len(nums))]
            trimmed.sort()
            answer.append(trimmed[k-1][1])
        return answer
