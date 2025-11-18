class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(names)
        for i in range(n):
            min_ind = i
            for j in range(i+1,n):
                if heights[j] > heights[min_ind]:
                    heights[j],heights[min_ind] = heights[min_ind],heights[j]
                    names[j], names[min_ind] = names[min_ind], names[j]
        return names





        