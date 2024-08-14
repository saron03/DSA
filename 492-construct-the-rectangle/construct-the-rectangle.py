class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        dic1={}
        for w in range(math.isqrt(area), 0 , -1):
                if area % w == 0:
                    l = area//w
                    dic1[l-w] = [l,w]
        min_value = float('inf')
        for key in dic1.keys():
            min_value = min(min_value, key)
        return dic1[min_value]
    