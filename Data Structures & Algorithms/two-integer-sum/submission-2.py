class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
                                     
        hmap={}

        for index,num in enumerate(nums):

            diff=target-num

            if diff in hmap:
               return [hmap[diff],index]
            hmap[num]=index
        
        return[-1,-1]