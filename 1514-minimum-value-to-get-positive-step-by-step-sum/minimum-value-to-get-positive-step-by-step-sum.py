class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_value, current_sum = 1, 0
        min_sum = float('inf')
    
        for num in nums:
            current_sum += num
            min_sum = min(min_sum, current_sum)
        
        if min_sum < 0:
            start_value = 1 - min_sum
    
        return start_value
