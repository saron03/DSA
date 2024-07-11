class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        count1 = {}
        count2 = {}
        for num in nums1:
            count1[num] = count1.get(num, 0) + 1
        for num in nums2:
            count2[num] = count2.get(num, 0) + 1
        diff1 = []
        for num in nums1:
            if num in count1 and num not in count2:
                diff1.append(num)
                del count1[num] 
        diff2 = []
        for num in nums2:
            if num in count2 and num not in count1:
                diff2.append(num)
                del count2[num] 
    
        return [diff1, diff2]
        


        