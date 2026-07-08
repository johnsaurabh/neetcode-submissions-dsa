class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap={}
        for idx, num in enumerate(nums):
            diff=target-num
            if diff in hmap:
                return [hmap[diff],idx]
            hmap[num]=idx
        return [-1,-1]


        