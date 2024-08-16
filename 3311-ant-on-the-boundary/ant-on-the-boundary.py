class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        count=0
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
            if nums[i] == 0:
                count +=1
        return count