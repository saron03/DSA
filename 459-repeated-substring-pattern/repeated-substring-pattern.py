class Solution(object):
    def repeatedSubstringPattern(self, s):
        if len(s) == 1:
            return False
        if len(set(s)) == 1:
            return True
        
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                unique = s[:i]
                if unique * (n // i) == s:
                    return True
        return False
