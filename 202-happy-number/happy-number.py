class Solution:
    def isHappy(self, n: int) -> bool:
        def squares(x):
            return sum(int(i) ** 2 for i in str(x))
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = squares(n)
        
        return n == 1



