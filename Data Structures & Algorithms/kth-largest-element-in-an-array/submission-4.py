class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums) - 1
        pivot = len(nums) - 1
        target = k - 1 #index of target if it was in sorted array
        

        while True:
            pivot = end
            i = start

            for j in range(start, end):
                if nums[j] > nums[pivot]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1

            nums[pivot], nums[i] = nums[i], nums[pivot]

            if i == target:
                return nums[i]
            elif i < target:
                start = i + 1
            else:
                end = i - 1

