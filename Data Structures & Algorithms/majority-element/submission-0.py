class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hmap=defaultdict(int)
        n=len(nums)
        for num in nums:
            hmap[num]+=1
            if hmap[num]> n/2:
                return num
            
        return 0


        