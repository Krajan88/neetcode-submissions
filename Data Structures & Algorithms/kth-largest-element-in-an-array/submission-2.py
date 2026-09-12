"""

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums) - 1
        
        target = k - 1 #k-1 not len(nums) - k

        while True:
            pivot = nums[end] 
            i = start

            for j in range(start, end):
                if nums[j] > pivot: #compare nums[j] to pivot, not nums[end].
                    nums[j], nums[i] = nums[i], nums[j]
                    i+=1

            #forgot to change pivot and i values at the end
            nums[i], nums[end] = nums[end], nums[i]

            if i == target:
                return nums[i]
            
            elif i > target:
                end = i - 1 #forgot to do -1

            elif i < target:
                start = i + 1