class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans= [0] * 2 *n
        for i in range(0,n):
            ans[i] = nums[i]
        j=0
        for i in range(n, n + n):
            ans[i] = nums[j]
            j +=1
        return ans

