class Solution(object):
    def coloredCells(self, n):
        i = 1
        if n ==1:
            return 1
        
        for j in range(1 , n):
            i+=(j*4)

        return i
