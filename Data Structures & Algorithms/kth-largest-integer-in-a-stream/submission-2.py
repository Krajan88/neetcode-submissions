class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        # print(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

        # print(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        print(self.minHeap)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        print(self.minHeap)
        print("-")

        return self.minHeap[0]