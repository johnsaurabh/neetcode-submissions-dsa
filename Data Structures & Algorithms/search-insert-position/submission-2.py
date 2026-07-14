class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lo=0
        hi=n-1

        while lo<=hi:
            mid=(hi+lo)//2

            if nums[mid]<target:
               lo=mid+1
            elif nums[mid]>target:
                hi=mid-1
            elif nums[mid]==target:
                return mid
        return lo