class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[nums[0]]
        k = n
        i = 1
        while i < n and k < len(nums):
            res.append(nums[k])
            res.append(nums[i])
            k +=1
            i+=1
        res.append(nums[k])
        return res