class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        res = float('inf')
        sum = 0
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                res = min(res,right - left + 1)
                sum -=nums[left]
                left +=1
            right +=1
        return 0 if res == float('inf') else res