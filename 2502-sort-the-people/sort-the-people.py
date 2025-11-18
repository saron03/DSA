class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(heights)

        for i in range(n):
            for j in range(1,n-i):
                if heights[j-1] < heights[j]:
                    temp = heights[j-1]
                    temp2 = names[j-1]
                    heights[j-1] = heights[j]
                    names[j-1] = names[j]
                    heights[j] = temp
                    names[j] = temp2
        return names


        