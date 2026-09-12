class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            maxHeap.append(-stone)

        heapq.heapify(maxHeap)

        print(maxHeap)

        while len(maxHeap) > 1:
            larger = heapq.heappop(maxHeap)
            smaller = heapq.heappop(maxHeap)           

            if smaller == larger:
                continue
            
            heapq.heappush(maxHeap, larger-smaller)


            
        
        if maxHeap:
            return -maxHeap[0]
        else:
            return 0