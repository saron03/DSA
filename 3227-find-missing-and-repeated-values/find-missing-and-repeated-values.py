class Solution(object):
    from collections  import defaultdict
    def findMissingAndRepeatedValues(self, grid):
        dic1=defaultdict(int)
        n = len(grid)
        sum = 0
        res=[]
        for i in range(1,n**2 +1):
            sum +=i
        for i in range(len(grid)):
            for j in grid[i]:
                dic1[j] +=1
                sum -=j
        for k in dic1:
            if dic1[k] > 1:
                res.append(k)
                sum = sum +k
                break
        res.append(sum)
        return res
            
        