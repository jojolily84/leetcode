class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry != 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            k = x + y + carry
            if k >= 2:
                result = str(k - 2) + result
                carry = 1
                
            else:
                result = str(k) + result
                carry = 0
            i -= 1
            j -= 1
        return result