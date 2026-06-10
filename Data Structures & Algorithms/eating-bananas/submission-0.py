class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            s = 0
            mid = (l + r)//2

            for i in range(len(piles)):
                s += math.ceil(piles[i] / mid)

            if s > h:
                l = mid + 1

            else:
                r = mid

        return l
