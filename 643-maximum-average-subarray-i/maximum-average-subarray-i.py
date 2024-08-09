class Solution(object):
    def findMaxAverage(self, nums, k):
        total = sum(nums[:k])
        average_max = float(total) / k
        for i in range(1, len(nums) - k + 1):
           total = total - nums[i - 1] + nums[i + k -1]
           average_max = max(average_max, float(total) / k)
        return average_max