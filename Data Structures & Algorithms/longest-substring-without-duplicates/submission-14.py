class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #set left pointer at 0 right pointer at 1
        #shift right pointer if there are no repeating characters
            #how to know that?: Create a set of the current characters
            #inside of the window

        #shift the left AND the right pointers if there is some repeating characters
        #repeat the process until you shift only right OR until end of the string
            #might actually just need to shift the left one too tired to check tho
        #keep track of the maximum length of the substring

        #oh I get it: We dont shift the right one when we find a duplicate because we might miss 
        #it in the next substring: say abac, with l=0 r=2, if we shift both, 
        #there are no a's inside anymore. but alas!
        # a would still be used within the substring to make bac
        
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        

        l = 0
        r = 0
        max_length, current_length = 0, 0
        window = set()

        
        
        while r < len(s):
            #what to do if we encounter a repeat 
            while s[r] in window:
                window.remove(s[l])
                l += 1
                


            #pwwkew

            window.add(s[r])

            max_length = max(len(window), max_length)
            

            #the case where the two pointers are at the same location (2 neighboring 
            #if l == r:
            #    window.clear()
            #    window.add(s[l])
            #    length = len(window)

            r+=1

        return max_length
        #max length will be the size of the biggest set so seperate length is not needed I dont thinjk
        
                

            



        