class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        if len(nums) == 3 :
            return nums[0]
        elif len(nums) > 3:
            return nums[-3]
        else:
            return nums[-1]

