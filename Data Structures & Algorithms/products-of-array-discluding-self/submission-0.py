class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j = len(nums)
        res = []
        lproduct = [1]*j
        rproduct = [1]*j
        
        

        
        
        for i in range(1, j):
            lproduct[i] = lproduct[i-1] * nums[i-1]

            rproduct[j-i-1] = rproduct[j-i] * nums[j-i]

        for i in range(0,j):
            res.append(rproduct[i] * lproduct[i])

        return res