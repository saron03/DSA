class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic1 ={}
        for i in nums:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        for key, value in dic1.items():
            if value > len(nums) // 2:
                return key
        return -1
