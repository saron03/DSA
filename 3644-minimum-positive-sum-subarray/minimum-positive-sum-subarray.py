class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float("inf")

        for i in range(n):
            current_sum = 0
            for j in range(i, min(i + r, n)):
                current_sum += nums[j]
                
                size = j - i + 1
                if l <= size <= r and current_sum > 0:
                    min_sum = min(min_sum, current_sum)

        return min_sum if min_sum != float("inf") else -1