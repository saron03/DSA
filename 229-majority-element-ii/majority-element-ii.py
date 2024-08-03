class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = defaultdict(int)
        result = []
        for num in nums:
            m[num] += 1
        n = len(nums) // 3
        for key, value in m.items():
            if value > n:
                result.append(key)
        
        return result