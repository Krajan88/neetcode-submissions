class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        1. Find a cycle within the list
        2. Find the index of the entrance to the cycle

        Rewatch the whole neetcode video again 
        """
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
