class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows=len(matrix)
        cols=len(matrix[0])

        lo=0
        hi=rows*cols-1

        while lo<=hi:

            mid=(lo+hi)//2

            row=mid//cols
            col=mid%cols
            
            if matrix[row][col]==target:
                return True

            if matrix[row][col]<target:
                lo=mid+1
            else:
                hi=mid-1
        return False