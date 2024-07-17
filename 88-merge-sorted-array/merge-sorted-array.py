class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer = 0
        for i in range(m, m + n):
            nums1[i] = nums2[pointer]
            pointer  +=1
        nums1.sort()