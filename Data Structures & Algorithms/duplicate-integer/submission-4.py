class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)

        if len(my_set) == len(nums):
            return False
        else:
            return True