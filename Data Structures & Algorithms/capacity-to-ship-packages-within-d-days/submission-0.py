class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo=max(weights)
        hi=sum(weights)
        result=hi


        while lo<=hi:

            mid=(lo+hi)//2

            current_load=0
            days_used=1

            for weight in weights:
                if current_load+weight<=mid:
                    current_load+=weight
                else:
                    days_used+=1
                    current_load=weight
            
          
            if days_used<=days:
                result=mid
                hi=mid-1
            else:
                lo=mid+1
        return result
            
                

            
        