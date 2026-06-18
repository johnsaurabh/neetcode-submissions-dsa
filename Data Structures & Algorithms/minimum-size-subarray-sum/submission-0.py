class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left=0
        current_sum=0
        result=float('inf')

        for right, num in enumerate(nums):
            current_sum+=num
            while current_sum>=target:

                result=min(result,right-left+1)
                current_sum-=nums[left]
                left+=1
        return result if result!=float('inf') else 0
                
