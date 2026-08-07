class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = (total+1)//2 #tells us the total elements in left partition

        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True: #we know a median is guaranteed so we can just return it once its found, no need to exit the loop
            i = (l+r)//2 #pointer for A
            j = half - i - 2 #pointer for B. J is supposed to be the number of elements in array B, we subtract 2 to get rid of the number shift caused by indexes (arrays are indexed at 0, i starts at 0 and j start at 0 so we have to subtract 2)

            #partitions

    #Why the -infinity / infinity edge cases? It's for the comparison of the endings of partitions of A and B. For instance, assume the split happens at i=0, which is the start of A (smaller array), meaning the smaller array would have no left partition. Since Aleft is compared against Bright, that there is no real number to compare to, we set Aleft to -infinity, so that the comparison is satisfied.

            Aleft = A[i] if i >= 0 else float("-infinity") #left value from a partition from A we compare to (the biggest value in the left partition)
            Aright = A[i+1] if (i+1) < len(A) else float("infinity") #right value from a partition A we compare to (the smallest value in the right partition)

            Bleft = B[j] if j >= 0 else float("-infinity")#right value from the left partition of B 
            Bright = B[j+1] if (j+1) < len(B) else float("infinity") #left value from the right partition of B

            #now for the algorithm, the endings of the left partitions msut be smaller than the right one (for the opposite partitions, as in Aleft < Bright and vice versa)

            print("i"+str(i))
            print("j"+str(j))
            print(Aleft)
            print(Aright)
            print(Bleft)
            print(Bright)
            print("------")
            
            if Bleft > Aright:
                l = i + 1
            elif Aleft > Bright:
                r = i - 1
            else:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
                else:
                    return max(Aleft, Bleft)




