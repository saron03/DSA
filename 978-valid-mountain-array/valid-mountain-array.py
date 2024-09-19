class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_num = -100
        max_index = -1
        res = True
        if len(arr) < 3:
            return False
        for i in range(len(arr)):
            if arr[i] >= max_num:
                max_num = arr[i]
                max_index = i
        if max_index == len(arr) -1 or max_index == 0:
            return False
        for i in range(1,max_index + 1):
            if arr[i] <= arr[i-1]:
                res = False
                break
        for i in range(max_index, len(arr)-1):
            if arr[i] <= arr[i+1]:
                res = False
                break
        return res

