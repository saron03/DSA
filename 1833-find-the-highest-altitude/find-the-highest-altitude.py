class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0] * (len(gain) + 1)
        high = res[0]
        for i in range(len(gain)):
            res[i +1] = res[i] + gain[i]
            high = max(high, res[i +1])
        return high

            