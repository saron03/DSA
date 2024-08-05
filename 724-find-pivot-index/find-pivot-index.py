class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == totalSum - left_sum - nums[i]:
                return i
            left_sum +=nums[i]
        return -1