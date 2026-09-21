class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sortedTasks = []
        time = 0
        heap = []
        res = []

        for i in range(len(tasks)):
            sortedTasks.append((tasks[i][0], tasks[i][1], i))

        i = 0

        sortedTasks = sorted(sortedTasks)
        


        heapq.heappush(heap, (sortedTasks[i][1], sortedTasks[i][2]))

        time = sortedTasks[i][0]  
        
        i += 1

        while len(res) < len(tasks):
            while i < len(tasks) and sortedTasks[i][0] <= time:
                #tuple (processing time, index). Added for every task that falls in current processing time
                heapq.heappush(heap, (sortedTasks[i][1], sortedTasks[i][2]))
                i += 1
                

            if not heap:
                heapq.heappush(heap, (sortedTasks[i][1], sortedTasks[i][2]))
                i += 1

            # print(i)
            # print(sortedTasks)
            # print(time)
            # print(heap)
            # print(".")

            task = heapq.heappop(heap)

            time += task[0]
            res.append(task[1])

        return res


        




"""
Python compares tuples lexicographically -- so for a tuple holding (processing time, index), if the processing times are the same, python will automatically look at the index

This property applies when heapifying a list of tuples as well.

1) sort the list by starting times (while keeping track of the original index)
2) set time to the lowest starting time
3) onto the heap, push all the tasks of that starting time as tuples (starting time, index)
    -python compares tuples lexographically -- if there exists two tasks of the same processing
     time, python will automatically put the one with the smaller index above the one with the
     larger index.
4) pop every element of the heap and append all the indicies to res
5) increment the time by processing time of each task
    -for every task that was added to res, you have to check the non-processed tasks again
     and append the ones where processing time <= current time

"""