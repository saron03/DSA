class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        run_sum = sum(nums[:k])
        run_average = run_sum /k
        for i in range(1,n-k+1):
            run_sum = run_sum - nums[i-1] + nums[i + k-1] 
            run_average = max(run_average, run_sum /k) 
        return run_average   



