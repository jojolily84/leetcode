class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n 
        #XOR 是 Bitwise Exclusive OR
        #a ^ a = 0      自己 XOR 自己 → 歸零
        #a ^ 0 = a      XOR 0 → 不變
        #a ^ b = b ^ a  交換律成立（順序不影響結果）
        #a ^ b = 1      a!=b
        return result
