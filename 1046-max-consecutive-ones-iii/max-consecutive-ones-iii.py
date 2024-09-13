class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
            i, j = 0, 0
            max_length = 0
            while i < len(nums):
                if nums[i] == 0:
                    k -= 1
                
                if k < 0:
                    if nums[j] == 0:
                        k += 1
                    j += 1
                max_length = max(max_length, i - j +1)
                i += 1
            
            return max_length