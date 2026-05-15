class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window = []
        res=[]
        
        for r in range(len(nums)):
            window.append(nums[r])
            
            if r-l+1 == k:
                res.append(max(window))
                window.pop(0)
                l+=1
                
        
        return res
            
                
                

            
            
            