class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distances = []

        #creating a tuple containg (distance, point)
        for point in points:
            distances.append((math.sqrt(point[0]**2 + point[1]**2), point))

        #first value of the heap is used as the values minHeap checks
        heapq.heapify(distances)

        #append the first k lowest distances to result
        for i in range(k):
            res.append(heapq.heappop(distances)[1])

        return res