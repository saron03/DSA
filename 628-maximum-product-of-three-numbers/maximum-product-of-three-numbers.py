class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
           return math.prod(nums)
        nums.sort()
        return max(math.prod(nums[-1:-4:-1]), math.prod(nums[0:3]), nums[0]*nums[1]*nums[-1])