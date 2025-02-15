class Solution(object):
    def intersection(self, nums1, nums2):
        nums2_set = set(nums2) 
        res = set()
        for num in nums1:  
            if num in nums2_set:  
                res.add(num) 
        return list(res)  
