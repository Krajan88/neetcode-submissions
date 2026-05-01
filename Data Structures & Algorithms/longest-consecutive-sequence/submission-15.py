class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        ongoing = 0
        longest = 0
        
        if len(nums) == 1:
            return 1

        for num in my_set:
            if num-1 not in my_set:
                ongoing = 1
                start = num
                
                while start+1 in my_set:
                    start+=1
                    ongoing += 1

            


            if ongoing > longest:
                longest = ongoing

        return longest

#
#
#Input: nums = [2,20,4,10,3,4,5]
#utput: 4