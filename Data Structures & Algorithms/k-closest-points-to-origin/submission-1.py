class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distances = []

        for point in points:
            distances.append((math.sqrt(point[0]**2 + point[1]**2), point))

        heapq.heapify(distances)

        for i in range(k):
            res.append(heapq.heappop(distances)[1])

        return res