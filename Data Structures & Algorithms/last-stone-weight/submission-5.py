class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)


        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)           

            if second == first:
                continue

            heapq.heappush(maxHeap, first-second)


        
        if maxHeap:
            return -maxHeap[0]
        else:
            return 0