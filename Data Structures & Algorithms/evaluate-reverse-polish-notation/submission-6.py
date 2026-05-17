class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        num = 0

        for element in tokens:
            match element:
                case "+":
                    num = stack.pop() + stack.pop()
                    stack.append(num)

                 
                case "-":
                    num = -stack.pop() + stack.pop()
                    stack.append(num)



                case "*":
                    num = stack.pop() * stack.pop()
                    stack.append(num)



                case "/":
                    temp = stack.pop() 
                    num = int(stack.pop() / temp)
                    stack.append(num)


                
                case _:
                    stack.append(int(element))
                    

            
            print(stack)

        return stack[0]