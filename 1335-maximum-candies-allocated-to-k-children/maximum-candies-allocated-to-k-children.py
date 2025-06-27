class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        l,r = 1, max(candies)
        res = 0

        while l <= r:
            m = (l+r)//2
            kids = 0
            for i in candies:
                kids += (i // m)
            if kids >= k:
                res = max(res, m)
                l = m +1
            else:
                r= m-1
        return res

