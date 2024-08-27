class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        i, j = 0, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i, j = 0, k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        f, g = k, n - 1
        while f < g:
            nums[f], nums[g] = nums[g], nums[f]
            f += 1
            g -= 1
        
        return nums






