class Solution(object):
    def minMoves(self, nums):
        count = 0
        total = sum(nums)
        min_num = min(nums)

        for i in nums:
            count += i - min_num

        return count

