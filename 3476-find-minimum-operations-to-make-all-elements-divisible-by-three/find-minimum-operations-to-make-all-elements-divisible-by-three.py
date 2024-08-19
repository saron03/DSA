class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            if i % 3 != 0:
                if i +1 % 3 == 0:
                    i +=1
                else:
                    i -=1
                count +=1
        return count