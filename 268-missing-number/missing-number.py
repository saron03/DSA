class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_no = 0
        n = len(nums)
        for i in range(0,n+1):
            if i not in nums:
                missing_no = i
        return missing_no