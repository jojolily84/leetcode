class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  #char -> 最後出現的 index
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            # 只有當重複字元的 index 落在目前 window 內才需要移動 left
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len
