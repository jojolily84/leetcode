class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd =0, 0
        index = 0
        num = n
        while num:
            if (num &1) == 1: #當前最低位的 bit 是 1，才進去處理
                if index % 2 ==0:
                    even += 1
                else:
                    odd += 1
            num >>= 1 
            # >> 是 bitwise right shift，把所有 bit 向右移動指定位數，最左邊補 0
            # 110010  >> 1  =  011001 (50 >> 1 = 25)
            # 011001  >> 1  =  001100 (25 >> 1 = 12)
            index += 1
        return [even, odd]
