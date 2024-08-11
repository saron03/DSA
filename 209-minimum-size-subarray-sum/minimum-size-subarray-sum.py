class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        minLen = float('inf')
        indexLeft = 0
        sub = []
        for i in range(len(nums)):
            sum += nums[i]
            sub.append(i)
            while sum >= target:
                minLen = min(minLen, len(sub))
                sum -= nums[indexLeft]
                sub.pop(0)
                indexLeft +=1
        return minLen if minLen != float('inf') else 0


