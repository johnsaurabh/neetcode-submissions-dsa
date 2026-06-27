class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
    
        n=len(nums)
        new_array=[0]*(2*n)
        

        for i in range(n):
            new_array[i]=nums[i]
            new_array[n+i]=nums[i]

        return new_array

        