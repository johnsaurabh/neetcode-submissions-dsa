class Solution:
    def maxArea(self, heights: List[int]) -> int:
      n=len(heights)
      left=0
      right=n-1
      max_water=0

      while left<=right:
        area=min(heights[left],heights[right])*(right-left)
        if heights[left]<heights[right]:
          left+=1
        else:
          right-=1
        max_water=max(max_water,area)
      return max_water




        
    