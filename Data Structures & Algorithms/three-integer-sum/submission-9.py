class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_nums = nums.copy()
        my_nums.sort()
        res = []

        
        if my_nums[0] > 0:
            return []

        for i in range(len(my_nums)-2):
            r = len(my_nums) - 1
            target = -1 * my_nums[i]

            l = i+1

            while l<r:
                s = my_nums[l] + my_nums[r]

                if s < target:
                    l+=1
                elif s > target:
                    r-=1
                elif s == target:
                    triplet = [my_nums[i], my_nums[l], my_nums[r]]
                    triplet.sort()
                    res.append(triplet)

                    l+=1
                    r-=1

            i+=1

        if not res:
            return []

        final = []

        for i in range(len(res)):
            if res[i] in final:
                continue
            else:
                final.append(res[i])

        return final


    






        #return all unique triplets that add up to 0
        #create 2 for loops: one that iterates throuhg elemtn from left to right
        #and anothre for loop for the two pointer
        #
        # make an if statement for when lowest number after sorting is non-zero, it must 
        # return an empty array

        # Let i = element in array from left to right and l/r be left and right pointers
        #for it to add up to 0, l + r = -i, becaues then i+(l+r) = i-i = 0
        
        #
        #so you basically have to do a 2sum problem for each i, where the target
        #sum for the two pointer is = i

        # create a seperate for loop to check for duplciates later

        # also, for the l element, it never has to go before the i element -- this would
        # just cause an unnecessary duplicate