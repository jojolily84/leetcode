class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(x,n):
            if n == 0:
                return 1
            helf = fast_pow(x, n // 2)
            if n % 2 == 0:
                return helf*helf
            else:
                return x*helf*helf
        
        if n < 0:
            x = 1 / x
            n = - n
        return fast_pow(x, n)
        