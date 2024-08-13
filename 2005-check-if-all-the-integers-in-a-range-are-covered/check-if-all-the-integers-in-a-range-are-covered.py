class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        res = False
        for i in range(left,right+1):
            for x in ranges:
                if x[0]<= i and x[1] >= i:
                    res = True
                    break
                else:
                    res = False
            if not res:
                return False
        return True
        
        
