class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(0, len(heights)):
            max = i
            for j in range(i+1, len(heights)):
                if heights[j]>heights[max]:
                    max = j
            
            heights[max] , heights[i] = heights[i], heights[max]
            names[i], names[max] = names[max], names[i]
        return names