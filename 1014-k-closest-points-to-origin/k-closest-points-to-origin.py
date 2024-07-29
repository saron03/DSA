class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_points = []
        for point in points:
            num1 = point[0]
            num2 = point[1]
            dis = math.sqrt(num1**2 + num2**2)
            distance_points.append((dis, point))

        distance_points.sort(key=lambda x: x[0])
        result = [point for (_, point) in distance_points[:k]]
        return result

