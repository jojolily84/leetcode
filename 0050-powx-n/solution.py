class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1
        helf = self.myPow(x, n // 2)
        if n % 2 == 0:
            return helf *helf
        else:
            return x * helf * helf
