class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        tempHash = {}
        time = 0

        for task in tasks:
            if task in tempHash:
                tempHash[task] += 1
            else:
                tempHash[task] = 1

        for key in tempHash:
            maxHeap.append((-tempHash[key], key))

        # print(maxHeap)

        heapq.heapify(maxHeap)

        while maxHeap:
            temp = []

            for i in range(n+1):
                #if there are still tasks available in the maxHeap
                if maxHeap:
                    freq, task = heapq.heappop(maxHeap)
                    time += 1

                    if freq + 1 < 0:
                        temp.append((freq+1, task))
                
                #if there are still tasks yet to be complete (meaning we haven't the whole 'tasks' list)
                elif temp:
                    time += 1

                #if no tasks to complete and we finished the entire current max heap
                else:
                    break    
      
            # This won't work for examples where n = 0, because temp only stored the most recently used task. Instead, you have to push every element onto the heap one by one
            #
            # maxHeap = temp    
            # heapq.heapify(maxHeap)

            for task in temp:
                heapq.heappush(maxHeap, task)


        return time
            


            



"""
Heap approach:

1) Store tasks in maxHeap of (frequency, task) in a maxHeap
2) Do heappop for n(or n+1? not sure) times OR until heap is empty
        -store these popped values with a decremented frequency now in some other array so that we can heapify it back
        -store those popped values also in a separate 'res' list (maybe not optimal, but want to try this at first)




"""