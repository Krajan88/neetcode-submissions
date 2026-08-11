class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in hashmap and hashmap[compliment]!=i:
                return [i, hashmap[compliment]]

        return None