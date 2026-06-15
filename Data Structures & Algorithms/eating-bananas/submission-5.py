class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        smallest = r
        

        while l < r:
            mid = (l+r)//2
            total = 0

            for i in range(len(piles)):
                total += math.ceil(piles[i]/mid)

            if total <= h:
                r = mid
            else:
                l = mid + 1

        return l
#goal: Find the lowest possible k that fits within h eating time