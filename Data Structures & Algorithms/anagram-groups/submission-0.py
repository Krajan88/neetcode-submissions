class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for i in range(len(strs)):
            count = [0] * 26

            #iterrates through all the characters of strings in strs
            for j in strs[i]:
                count[ord(j)-97]=count[ord(j)-97]+1


            key = tuple(count)
            
            my_dict[key].append(strs[i])

        return list(my_dict.values())

        




#so list(my_dict.values()) would create a list of all the values of key-value pairs in a dictionary