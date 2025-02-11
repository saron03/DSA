class Solution(object):
    from collections import defaultdict
    def equalPairs(self, grid):
        dic1 = defaultdict(list)
        n =len(grid)
        for j in range(n):
            for i in range(n):
                dic1[j].append(grid[i][j])
        count = 0
        for i in range(len(dic1)):
            for j in range(len(grid)):
                if(dic1[i] == grid[j]):
                    count +=1
        return count
        