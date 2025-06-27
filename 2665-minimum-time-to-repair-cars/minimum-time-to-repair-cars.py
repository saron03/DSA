class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l,r = 1, (max(ranks) * cars**2)
        res = float("inf")

        while l <= r:
            m = (l+r)//2
            n = 0
            for i in ranks:
                n += int(sqrt(m/i))
            if n >= cars:
                res = min(res,m)
                r = m-1
            else:
                l = m +1
        return res

