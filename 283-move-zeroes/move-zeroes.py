class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for l in range(len(nums)):
            if nums[l] != 0:
                nums[i] = nums[l]
                i +=1
        
        for j in range(i, len(nums)):
            nums[j] = 0
