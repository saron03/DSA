class Solution(object):
    def sortPeople(self, names, heights):
        for i in range(1, len(heights)):
            temp = heights[i]
            tempn = names[i]
            j = i -1
            while j >=0:
                if heights[j] < temp:
                    heights[j+1] = heights[j]
                    names[j+1] = names[j]
                    j -=1
                else:
                    break
            heights[j+1] = temp
            names[j+1] = tempn
        return names