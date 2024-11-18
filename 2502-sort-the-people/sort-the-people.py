class Solution(object):
    def sortPeople(self, names, heights):
        for i in range(len(heights) -1):
            min_ind = i
            for j in range(i+1, len(heights)):
                if heights[j] > heights[min_ind]:
                    min_ind = j
            if min_ind != i:
                heights[i], heights[min_ind] = heights[min_ind], heights[i]
                names[i], names[min_ind] = names[min_ind], names[i]
        return names