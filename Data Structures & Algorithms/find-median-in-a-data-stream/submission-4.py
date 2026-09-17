class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        if not self.small or -num >= self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        #too many numbers in small        
        if len(self.small) - len(self.large) > 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        #too many numbers in large
        elif len(self.large) - len(self.small) > 1:
            val = -heapq.heappop(self.large)
            heapq.heappush(self.small, val)

        

    def findMedian(self) -> float:
        

        if (len(self.large) + len(self.small)) % 2: #odd, since 0 is false
            if len(self.large) > len(self.small):
                return self.large[0]
            else:
                return -self.small[0]
        else: #even
            return (self.large[0] - self.small[0]) / 2

        