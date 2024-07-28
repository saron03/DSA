class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr=[]
        for i in range(len(points)):
            arr.append(points[i][0])
        
        arr.sort()
        max = 0
        for i in range(len(arr) -1):
            if arr[i+1] - arr[i] > max:
                max = arr[i+1] - arr[i] 
        return max
