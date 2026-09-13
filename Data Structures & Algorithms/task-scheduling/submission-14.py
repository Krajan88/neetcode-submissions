class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}
        time = 0

        #frequency:task hashmap
        for task in tasks:
            if task in hashMap:
                hashMap[task] += 1
            else:
                hashMap[task] = 1

        maxHeap = []

        #max heap made of tuples where  0-freq and 1-task
        for task in hashMap:
            maxHeap.append((-hashMap[task], task))

        heapq.heapify(maxHeap)

        while maxHeap:
            temp = []
            #numebr of tasks in size of n
            for i in range(n+1):
                if maxHeap:
                    freq, task = heapq.heappop(maxHeap)
                    time += 1

                    if freq + 1 < 0:
                        temp.append((freq + 1, task))

                elif temp: #required here because if maxHeap empty, and nothing was stored in temp, we are at the end of tasks
                    time += 1
                
                # else:
                #     break
                
            for task in temp:
                heapq.heappush(maxHeap, task)

        return time