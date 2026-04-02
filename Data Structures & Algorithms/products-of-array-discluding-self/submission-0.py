class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        prefix=1
        n=len(nums)
        output=[1]*n
        
        for i in range(len(nums)):
            output[i]=prefix
            prefix*=nums[i]
            
        
        postfix=1
        for i in range(n-1,-1,-1):
            output[i]*=postfix
            postfix*=nums[i]
            
        
        return output
        