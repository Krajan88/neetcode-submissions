class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0

        #frequency tables for characters in the required string and the window
        freq_t = {}
        freq_s = {}

        #the shortest valid substring (just use len() to compare the current
        #                              valid one and the shortest one)
        min_substring = ""


        #character frequency for the required substring
        for element in t:
            freq_t[element] = 1 + freq_t.get(element, 0)

        for key in t:
            freq_s[key] = 0

        while r < len(s):
            #frequency of required characters present in the string
            if s[r] in freq_t:
                freq_s[s[r]] = 1 + freq_s.get(s[r], 0)

            #check whether all required characters and their frequency is in s
            while all(freq_s[c] >= freq_t[c] for c in freq_t):
                if min_substring == "":
                    min_substring = s[l:r+1]

                
                if len(s[l:r+1]) < len(min_substring):
                    min_substring = s[l:r+1]
                    

                    print(str(l) + "|" + str(r) + "|" + min_substring + str(freq_s))

                    
                #non-required characters not included so wouldn't be able to decrement

                if s[l] in freq_s:
                    freq_s[s[l]] -= 1
                
                l+=1

            #r+1 since splicing is exclusivew
            
                
            else:
                r+=1

            

            

        return min_substring



