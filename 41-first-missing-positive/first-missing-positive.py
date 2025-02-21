class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxNum = float('-inf')
        for i in nums:
            if i > maxNum:
                maxNum = i
        if maxNum < 0:
            return 1
        nums = set(nums)
        for i in range(1,maxNum+1):
            
            if i not in nums:
                return i
        return maxNum +1