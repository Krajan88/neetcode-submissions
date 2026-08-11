class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""

        for element in strs:
            word = word + str(len(element)) + "#" + element
        return word

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        j = 0

        while j < len(s):
            i = j

            while s[j] != "#":
                j+=1


            length = (int)(s[i:j])

            i=j+1
            j+=length+1

            strs.append(s[i:j])
        
        return strs


# neet code hi
# 4#neet4#code2#hi
# i - length of encoded string
# j - length of each word (number before the #)

# Note for what this question is even asking you to do:
# encoding - turning list into a string
# decoding - turning that string back into a list
#
# When encoding you need to keep track of length of the word
#  -do that by storing length of word behind a delimeter for each word
#     i.e neet code -> 4#neet4#code

#4#neet4#code
#i=j
#while string != # {
#j+=1
#}
#length = string[i:j]
#i=j+1
#j+=length + 1





