class Solution:
    def trap(self, height: List[int]) -> int:
        maxh = 0
        res = 0
        prefix_max = []
        suffix_max = []

        #left bound always has 0 as lowest prefix (does not exist)
        if len(height) > 0:
            prefix_max.append(0)
            suffix_max.append(0)

        for i in range(len(height)-1):
            if maxh > height[i]:
                prefix_max.append(maxh)
            else:
                maxh = height[i]
                prefix_max.append(maxh)
        
        maxh = 0        

        for i in range(len(height)-1, 0, -1):
            if maxh > height[i]:
                suffix_max.append(maxh)
            else:
                maxh = height[i]
                suffix_max.append(maxh)

        suffix_max.reverse()

        for i in range(len(height)-1):
            num = min(suffix_max[i],prefix_max[i]) - height[i]

            if num > 0:
                res += num

        return res

#min (height[l], height[r]) - height[i], where l and r are indicies of
#max height left and right
#
#Regular  = [0,2,0,3,1,0,1,3,2,1]
#Left max = [0,0,2,2,3,3,3,3,3,3]
#Rightmax = [3,3,3,3,3,3,3,2,1,0]

# When regular > smaller of the suffix/prefix, 
# the water is basically covered up by 
# the black boxes if it makes sense
