class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        run_average = float("-inf")
        run_sum = 0
        for i in range(k):
            run_sum += nums[i]
        run_average = max(run_average, run_sum /k)
        for i in range(1,n-k+1):
            run_sum = run_sum - nums[i-1] + nums[i + k-1] 
            run_average = max(run_average, run_sum /k) 
        return run_average   



