class Solution:
    def mySqrt(self, x: int) -> int:

        lo=0
        hi=x


        while lo<=hi:
            mid=(hi+lo)//2

            if mid*mid<x:
                lo=mid+1
            elif mid*mid>x:
                hi=mid-1
            elif mid*mid==x:
                return mid
        return hi
        