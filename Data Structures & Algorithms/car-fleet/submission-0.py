class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = len(position)
        stack = []
        times = [0.0] * cars
        tuples = []

        #positoin and speed stored as a tuple for each car and then sorted in descending order
        for i in range(cars):
            tuples.append((position[i], speed[i]))

        tuples.sort(reverse=True)

        #times the cars would reach the end by themselves
        for i in range(cars):
            times[i] = (target - tuples[i][0])/tuples[i][1]


        #stack logic
        for i in range(cars):
            if not stack or times[i] > stack[-1]:
                stack.append(times[i])


        print(tuples)
        print(times)

        return len(stack)

        
