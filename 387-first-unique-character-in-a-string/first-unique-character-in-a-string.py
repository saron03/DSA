class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic1 = {}
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = 1
            else:
                dic1[s[i]] += 1
        for i in range(len(s)):
            if dic1[s[i]] == 1:
                return i  
        
        return -1 

            
