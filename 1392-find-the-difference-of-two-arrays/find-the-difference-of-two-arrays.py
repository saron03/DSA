class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashtable = {}
        first_true_second_false = []
        second_true_first_false = []
        for num in nums1:
            if num not in hashtable:
                hashtable[num] = [True,False]
        for num in nums2:
            if num in hashtable:
                hashtable[num][1] = True
            else:
                hashtable[num] = [False,True]
        for key, value in hashtable.items():
            if value[0] and not value[1]:
                first_true_second_false.append(key)
            elif not value[0] and value[1]:
                second_true_first_false.append(key)
        return [first_true_second_false,second_true_first_false]
        
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        