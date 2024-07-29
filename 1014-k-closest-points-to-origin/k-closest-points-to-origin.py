class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(point, sqrt(point[0]**2 + point[1]**2)) for point in points]
        distances.sort(key=lambda x: x[1])
        return [point for point, distance in distances[:k]]