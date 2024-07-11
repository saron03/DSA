class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = [-1,-1]
        left= []
        right=[]
        for i in nums1:
            if i not in nums2 and i not in left:
                left.append(i)
        for j in nums2:
            if j not in nums1 and j not in right:
                right.append(j)  
        
        output[0]= left
        output[1] = right
        return output