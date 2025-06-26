# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 0, n
        while l <= r:
            m = (l+r) //2
            if isBadVersion(m):
                if l == r:
                    return l
                r = m
            else:
                l = m +1
                