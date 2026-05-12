class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        lo=0
        hi=n-1

        while lo<hi:
            mid=(lo+hi)//2

            if nums[mid]<nums[hi]:
                hi=mid
            elif nums[mid]>nums[hi]:
                lo=mid+1

            else:
                h-=1
        return nums[lo]



  