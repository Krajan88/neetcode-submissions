class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        num = 0

        for element in tokens:
            match element:
                case "+":
                    num = stack.pop() + stack.pop()
                    stack.append(num)
                    num = 0
                 
                case "-":
                    num = -stack.pop() + stack.pop()
                    stack.append(num)
                    num = 0


                case "*":
                    num = stack.pop() * stack.pop()
                    stack.append(num)
                    num = 0


                case "/":
                    temp = stack.pop() 
                    num = int(stack.pop() / temp)
                    stack.append(num)
                    num = 0

                
                case _:
                    stack.append(int(element))
                    

            
            print(stack)

        return stack[0]