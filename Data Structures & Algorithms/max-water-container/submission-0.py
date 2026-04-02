class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_water=0
        n=len(heights)
        l=0
        r=n-1
        i=0


        while l<r:
            
            water_held= (r-l) * min(heights[l],heights[r])

            if water_held>max_water:
                max_water=water_held
                
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_water
                