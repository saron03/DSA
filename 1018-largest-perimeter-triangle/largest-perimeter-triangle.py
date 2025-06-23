class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums) - 1
        while i >= 2:
            a, b, c = nums[i], nums[i-1], nums[i-2]
            if b + c > a:  
                return a + b + c
            i -= 1
        
        return 0
