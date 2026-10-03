class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        prefix=1
        n=len(nums)

        for i in range(n):
            result[i]=prefix
            prefix*=nums[i]

        suffix=1

        for i in range(n-1,-1,-1):
            result[i]*=suffix
            suffix*=nums[i]

        return result
        