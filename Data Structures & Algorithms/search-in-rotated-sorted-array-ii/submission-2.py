class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        n=len(nums)
        lo=0
        hi=n-1

        while lo<=hi:

            mid=(lo+hi)//2

            if nums[mid]==target:
                return True
            
            if nums[lo]==nums[mid]==nums[hi]:
                lo+=1
                hi-=1
                continue
            
            if nums[lo]<=nums[mid]:

                if nums[lo]<=target<nums[mid]:
                    hi=mid-1
                else:
                    lo=mid+1
            else:
                if nums[mid]<target<=nums[hi]:
                    lo=mid+1
                else:
                    hi=mid-1
        return False
        