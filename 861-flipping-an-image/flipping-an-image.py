class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output = []
        for i in range (len(image)):
            output.append( image[i][::-1])
        
        for i in range (len(output)):
            for j in range (len(output[i])):
                if output[i][j] == 0:
                    output[i][j] = 1
                else:
                    output[i][j] = 0
        
        return output