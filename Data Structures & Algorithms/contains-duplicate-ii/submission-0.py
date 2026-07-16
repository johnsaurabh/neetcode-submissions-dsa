class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
       
        seen={}

        for idx,num in enumerate(nums):

            if num in seen:
                if abs(idx-seen[num])<=k:
                    return True
            seen[num]=idx
        return False

