class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic1 = {}
        for i in s:
            dic1[i] = dic1.get(i,0) + 1
    
        for i in range(len(s)):
            if dic1[s[i]] == 1:
                return i  
        
        return -1 

            
