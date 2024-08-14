class Solution:
    def isUgly(self, n: int) -> bool:
        ugly=[2,3,5]
        product=1
        if n <= 0:
            return False
        for factor in [2,3,5]:
            while n % factor == 0:
                n = n // factor
        return n == 1
            
