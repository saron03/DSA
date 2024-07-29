class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1= {}
        dic2= {}
        for i in range(len(nums1)):
            if nums1[i] not in dic1:
                dic1[nums1[i]] = 1
            else:
                dic1[nums1[i]] += 1

        for i in range(len(nums2)):
            if nums2[i] not in dic2:
                dic2[nums2[i]] = 1
            else:
                dic2[nums2[i]] += 1
        result = []
        for num in dic1:
            if num in dic2:
                min_count = min(dic1[num], dic2[num])
                result.extend([num] * min_count)
        return result
        