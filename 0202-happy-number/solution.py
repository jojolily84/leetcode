class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10  #個位數
                total += digit **2
                num //= 10  #去掉個位數
            return total
        
        seen = set()
        while n != 1:
            if n in seen:  #重複出現,cycle
                return False
            seen.add(n)
            n = get_next(n)
        return True
