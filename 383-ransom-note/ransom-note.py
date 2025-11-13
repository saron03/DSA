class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dic1 = defaultdict(int)
        for n in magazine:
            dic1[n] +=1
        
        for k in ransomNote:
            if dic1[k] > 0:
                dic1[k] -=1
            else:
                return False

        return True
        
