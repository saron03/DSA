class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = [[], []]
        for i in nums1:
            if i not in nums2 and i not in output[0]:
                output[0].append(i)
        for j in nums2:
            if j not in nums1 and j not in output[1]:
                output[1].append(j)  
        return output