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

