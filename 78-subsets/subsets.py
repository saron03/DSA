class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i,arr):
                
            ans.append(arr.copy())
            for j in range(i,len(nums)):
                backtrack(j+1,arr + [nums[j]] )

        backtrack(0,[])
        return ans