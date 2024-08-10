class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        res=""
        count = 0
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        for i in range(n):
            if s[i] not in res:
                res += s[i]
            else:
                count = max(len(res),count)
                while s[i] in res:
                    res = res[1:]
                res +=s[i]
        count = max(len(res), count)
        return count
                

            
