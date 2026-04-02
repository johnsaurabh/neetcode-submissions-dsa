class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l,h=0,(m*n)-1

        while l<=h:
            mid=(l+h)//2
            row= mid//n
            col= mid % n
            mid_val=matrix[row][col]

            if target>mid_val:
                l=mid+1
            elif target<mid_val:
                h=mid-1
            else:
                return True
        return False
        