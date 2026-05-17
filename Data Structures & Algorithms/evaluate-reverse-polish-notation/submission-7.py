class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        num = 0

        for element in tokens:
            match element:
                case "+":
                    stack.append(stack.pop() + stack.pop())

                 
                case "-":
                    stack.append(-stack.pop() + stack.pop())



                case "*":
                    stack.append(stack.pop() * stack.pop())



                case "/":
                    temp = stack.pop() 
                    stack.append(int(stack.pop() / temp))

                case _:
                    stack.append(int(element))

        return stack[0]