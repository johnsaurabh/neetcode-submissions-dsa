class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[0]*2*n

        for i in range(n):
            arr[i]=nums[i]
            arr[n+i]=nums[i]

        return arr
        

        