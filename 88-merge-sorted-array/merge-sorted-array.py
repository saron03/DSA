class Solution(object):
    def merge(self, nums1, m, nums2, n):
        res = []
        j, k = 0, 0
        while j < m and k < n:
            if nums1[j] < nums2[k]:
                res.append(nums1[j])
                j += 1
            else:
                res.append(nums2[k])
                k += 1
        
        # Append the remaining elements from nums1 and nums2
        res.extend(nums1[j:m])
        res.extend(nums2[k:n])
        
        # Copy the merged result back to nums1
        nums1[:m+n] = res
