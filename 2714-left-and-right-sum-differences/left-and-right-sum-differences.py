class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftarr = [0] * len(nums)
        rightarr=[0] * len(nums)
        res= [0] *len(nums)
        for i in range(1,len(nums)):
            leftarr[i] = leftarr[i-1] + nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            rightarr[i] = rightarr[i +1] + nums[i + 1]
        for i in range(len(nums)):
            res[i] = abs(leftarr[i] - rightarr[i])
        return res


        


