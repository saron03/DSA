class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        new = []
        i, j = 0, 0
        
        # Merging two sorted arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new.append(nums1[i])
                i += 1
            else:
                new.append(nums2[j])
                j += 1
        
        # Append remaining elements from nums1
        while i < len(nums1):
            new.append(nums1[i])
            i += 1
        
        # Append remaining elements from nums2
        while j < len(nums2):
            new.append(nums2[j])
            j += 1
        
        # Find median
        n = len(new)
        if n % 2 == 0:
            x = n // 2
            y = x - 1
            mid = (new[x] + new[y]) / 2.0
        else:
            z = n // 2
            mid = new[z]
        
        return mid

