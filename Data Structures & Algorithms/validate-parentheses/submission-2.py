class Solution:
    def isValid(self, s: str) -> bool:
        #odd length s can never be balanced
        if(len(s)%2 != 0):
            return False
        
        close_to_open = {")":"(", "}":"{", "]":"["}
        stack = []

        for bracket in s:
            #if closing bracket
            if bracket in close_to_open:
                if not stack:
                    return False

                #check whether the top open bracket corresponds to the current closing bracket
                if stack[-1] == close_to_open[bracket]:
                    stack.pop()

                else:
                    return False


            #if opening bracket
            else:
                stack.append(bracket)


        if not stack:
            return True
        else:
            return False