class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for j in range(len(nums)):
            for i in range(j + 1 ,len(nums)):
                if nums[i] + nums[j] < target:
                    count +=1
        return count


