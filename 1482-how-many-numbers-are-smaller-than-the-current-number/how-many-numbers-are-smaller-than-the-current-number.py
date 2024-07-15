class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 and len(nums) == 1:
            return nums
        result= [0] * len(nums)
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums [i]:
                    count +=1
            result[i] = count

        return result