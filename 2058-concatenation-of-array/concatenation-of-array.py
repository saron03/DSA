class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans= [0]*2*n
        j = 0
        for i in nums:
            ans[j] = i
            ans[j+n] = i
            j +=1
        return ans