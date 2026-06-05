class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack=[]
        max_area=0
        heights.append(0)

        for i in range(len(heights)):
            if not stack or heights[i]>= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i]<heights[stack[-1]]:

                    idx=stack.pop()
                    height=heights[idx]
                    if stack:
                        left_wall=stack[-1]
                    else:
                        left_wall=-1
                    right_wall=i
                    area=height* (right_wall-left_wall-1)
                    max_area=max(area,max_area)
                stack.append(i)
        return max_area
