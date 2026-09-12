class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            maxHeap.append(-num)

        heapq.heapify(maxHeap)

        for i in range(k):
            res = heapq.heappop(maxHeap)

        return -res

        