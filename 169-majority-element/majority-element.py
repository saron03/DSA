class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        dic1 = defaultdict(int)
        ans = 0
        for num in nums:
            dic1[num] +=1
            if dic1[num] > n/2:
                ans = num

        return ans