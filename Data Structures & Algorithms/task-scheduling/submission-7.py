class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        tempHash = {}

        for task in tasks:
            if task in tempHash:
                tempHash[task] += 1
            else:
                tempHash[task] = 1

        for task in tempHash:
            maxHeap.append((-tempHash[task], task))

        heapq.heapify(maxHeap)

        time = 0

        while maxHeap:
            temp = []

            for i in range(n + 1):

                if maxHeap:
                    freq, task = heapq.heappop(maxHeap)

                    time += 1

                    if freq + 1 < 0:
                        temp.append((freq + 1, task))

                elif temp:
                    time += 1

                else:
                    break

            for item in temp:
                heapq.heappush(maxHeap, item)

        return time