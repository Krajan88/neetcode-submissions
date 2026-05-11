class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #fixed sliding window
        #keep track of frequencies of characters in s1 and iterate through
        #s2 and find a window with the same frequencies

        #if you cant find it return false
        #also you can use max() because there are 26 characters which makes it O(1)
        l, r = 0, 0
        window_size = len(s1)
        freq_1 = {}
        freq_2 = {}


        m = len(s1) - 1

        #iterates and populates the frequency table for the s1 substring
        for element in s1:
            freq_1[element] = 1 + freq_1.get(element,0)

        
        #i is the right pointer I think since it needs to increase every iteration anyways
        
        #s1="ab"
        #s2="lecabee"

        print(m)

        while r < len(s2):
            if r - l <= m:
                freq_2[s2[r]] = 1 + freq_2.get(s2[r], 0)
                r+=1
            else:
                freq_2[s2[r]] =  1 + freq_2.get(s2[r], 0)
                freq_2[s2[l]] -= 1

                if freq_2[s2[l]] == 0:
                    del freq_2[s2[l]]

                r+=1
                l+=1
                
            

            if freq_2 == freq_1:
                return True
            
        
        return False


        #how to find window that holds the same frequencies:
        #   all the frequencies in freq_2 must contain at least all elements of s1
        
        #If element not in s1 frequency, shift left poitner right (and right poitner
        #to that spot too)

        #if the element of s1 is in s2, start shifting the right pointer

        #how long do we shift the right pointer until?
        #-we encounter a character that was not in s1
        #-one of characters' frequency exceeds the frequency from s1
    

            