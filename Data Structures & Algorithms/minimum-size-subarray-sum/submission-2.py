class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
       
        current_sum=0
        n=len(nums)
        result=n+1
        left=0

        for right, num in enumerate(nums):

            current_sum+=num

            while current_sum>=target:

                result=min(right-left+1,result)
                current_sum-=nums[left]
                left+=1
                
        return result if result<=n else 0

                

       


