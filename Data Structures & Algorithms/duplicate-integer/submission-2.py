class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set(nums)

        if len(numbers) == len(nums):
            return False
        return True