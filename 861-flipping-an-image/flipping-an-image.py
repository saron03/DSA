class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            l = 0
            r = len(i) -1
            while l < len(i) and r > -1 and l < r:
                i[l] , i[r] = i[r], i[l]
                l +=1
                r -=1
            
            for k in range(len(i)):
                if i[k] == 0:
                    i[k] = 1
                else:
                    i[k] = 0
        return image
