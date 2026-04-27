class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        needle = min(strs)
        result = ""
        for j in range(len(needle)):
            for i in range(len(strs)):
                if strs[i][j] != needle[j]:
                    return result
            result += needle[j]
        return result