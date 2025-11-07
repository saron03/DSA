class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        dic1=defaultdict(int)

        for i in s:
            dic1[i] +=1
        
        for i in range(len(s)):
            if dic1[s[i]] == 1:
                return i
        
        return -1
