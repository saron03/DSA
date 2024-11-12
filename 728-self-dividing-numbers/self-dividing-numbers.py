class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left,right + 1):
            res = True
            for j in str(i):
                if j == "0" or i % int(j) != 0:
                    res = False
                    break
            
            if res:
                result.append(i)

        return result