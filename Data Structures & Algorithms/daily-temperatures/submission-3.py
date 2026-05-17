class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stores days / indexes of temperatures
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            #if stack is empty OR top of the stack is greater than current temp
            if not stack or temperatures[stack[-1]] > temperatures[i]:#not sure whether it'll be >= or just >
                stack.append(i) #storing days not temperatures

                
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    top = stack.pop()
                    res[top] = i - top
                    #add logic for actually computing the days
                stack.append(i)
               
                

        return res