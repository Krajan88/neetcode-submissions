class Solution:
    def maxArea(self, heights: List[int]) -> int:
        top_area = 0
        l = 0
        r = len(heights) - 1 

        while l<r:
            h = min(heights[l],heights[r])
            current_area = (r-l)*h

            if heights[l] <= heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1

            if current_area > top_area:
                top_area = current_area
        
        return top_area




    
#compare left and right sides
#keep track of highest area

#shift the side that's shorter closer to the center and track that
#current area
