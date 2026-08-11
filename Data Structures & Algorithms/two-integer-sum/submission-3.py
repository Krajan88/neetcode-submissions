class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        temp = 0

        for i in range(len(nums)):
            temp = target - nums[i]

            if temp in my_dict:
                return [my_dict[temp],i]
            else:
                my_dict[nums[i]] = i


            