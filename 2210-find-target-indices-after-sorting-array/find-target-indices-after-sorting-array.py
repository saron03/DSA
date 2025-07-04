class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        small=0
        count=0
        arr=[]
        for i in range(len(nums)):
            if nums[i] < target:
                small +=1
            elif nums[i] == target:
                count +=1
        
        while count !=0:
            arr.append(small)
            small +=1
            count -=1
        return arr
