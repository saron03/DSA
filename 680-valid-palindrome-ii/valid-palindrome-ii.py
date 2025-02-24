class Solution(object):
    def validPalindrome(self, s):
        i,j= 0, len(s) -1
        while i <= j:
            if s[i] == s[j]:       
                i+=1
                j-=1
            else:
                s1 =s[:i] + s[i+1:]
                s2 = s[:j] +s[j+1:]
                return  s1 ==  s1[::-1] or  s2 == s2[::-1]
        return True
        