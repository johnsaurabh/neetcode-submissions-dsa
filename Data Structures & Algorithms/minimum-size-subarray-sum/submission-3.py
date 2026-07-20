class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        current_sum=0
        result=float('inf')
        n=len(nums)
        left=0

        for idx,num in enumerate(nums):

            current_sum+=num


            while current_sum>=target:
                result=min(idx-left+1,result)
                current_sum-=nums[left]
                left+=1
        return result if result!= float('inf') else 0
        
            


        