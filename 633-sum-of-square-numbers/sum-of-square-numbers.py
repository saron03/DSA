class Solution(object):
    def judgeSquareSum(self, c):
        left, right = 0,int(c**0.5)
        ans = 0
        while left <= right:
            ans = left**2 + right**2
            if ans == c:
                return True
            elif ans > c: 
                right -=1
            else:
                left +=1
        return False
