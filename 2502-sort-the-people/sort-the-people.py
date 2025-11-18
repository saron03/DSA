class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(names)
        for i in range(n):
            min_ind = i
            for j in range(i+1,n):
                if heights[j] > heights[min_ind]:
                    min_ind = j
            heights[i],heights[min_ind] = heights[min_ind],heights[i]
            names[i], names[min_ind] = names[min_ind], names[i]
        return names





        