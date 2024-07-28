class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = []
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i] == target:
                arr.append(i)
        arr.sort()    
        return arr