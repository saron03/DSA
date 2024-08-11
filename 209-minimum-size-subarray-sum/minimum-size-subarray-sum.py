class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        minLen = float('inf')
        indexLeft = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                minLen = min(minLen, i - indexLeft + 1)
                if minLen == 1: return 1
                sum -= nums[indexLeft]
                indexLeft +=1
        return minLen if minLen != float('inf') else 0


