class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict = {}
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i!=j and nums[i] > nums[j] :
                    count+=1
            dict[i] =  count
        
        result = [dict[i] for i in range(len(nums))]
        return result