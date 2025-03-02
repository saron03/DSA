class Solution(object):
    def mergeArrays(self, nums1, nums2):
        res=[]
        i,j = 0,0
        while i < len(nums1) and j <len(nums2):
            if nums1[i][0] > nums2[j][0]:
                res.append(nums2[j])
                j+=1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i+=1
            else:
                num = nums1[i][1] + nums2[j][1]
                res.append([nums1[i][0], num])
                i+=1
                j+=1

        while i < len(nums1):
            res.append(nums1[i])
            i+=1
        while j < len(nums2):
            res.append(nums2[j])
            j+=1
        return res
        
            

            
