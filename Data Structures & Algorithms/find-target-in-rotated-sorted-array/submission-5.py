class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        
        split = l
#the seperation is at l
#now to figure out which subarray to use. You could compare the target to the boundaries of the 2 iguess
# (you only have to do this if l =/= 0 otherwise just do a binary search right away)

#array 1: l = 0 , r = split (where split = l)
#array 2: l = split, r = len(nums) - 1


        #i guess here we'er just determining the boundaries not doing the actual binary search logic
        if split == 0:
            #already sorted array, do a regular ass binary search
            l = 0
            r = len(nums) - 1
        else:
            if target >= nums[0] and target <= nums[split-1]:
                #search leftside array
                l = 0
                r = split-1

            else:
                #search rightside array
                l = split
                r = len(nums) - 1
            
        

    
        print(l)
        print(r)
        while l <= r:

            mid = (l+r)//2      

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        
        
        return -1


