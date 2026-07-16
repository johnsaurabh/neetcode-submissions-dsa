class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        lo=1
        hi=max(piles)
        result=0

        while lo<=hi:
            mid=(lo+hi)//2

            total_hours= sum( math.ceil(p/mid) for p in piles)

            if total_hours<=h:
                result=mid
                hi=mid-1
            else:
                lo=mid+1
        return result
