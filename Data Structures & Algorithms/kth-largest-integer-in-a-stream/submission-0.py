class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        res = sorted(self.nums)
        size = len(self.nums)

        return res[size - self.k]



        
