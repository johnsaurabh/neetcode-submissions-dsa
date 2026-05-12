class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo=0
        hi=len(nums)-1

        while lo<hi:
            mid=(lo+hi)//2

            if nums[mid]>nums[hi]:

                if nums[lo]<=target and target<=nums[mid]:
                    hi=mid
                else:
                    lo=mid+1
            
            elif nums[mid]<nums[hi]:

                if nums[mid]<target and target<=nums[hi]:
                    lo=mid+1

                else:
                    hi=mid
        return lo if target==nums[lo] else -1



            

