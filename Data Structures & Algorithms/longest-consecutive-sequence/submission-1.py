class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset= set()

        if len(nums)==0:
            return 0
        
        max_length=1

        for num in nums:
            numset.add(num)

        for num in nums:

            if num-1 not in numset:
                count=1

                current=num

                while current+1 in numset:
                    count+=1
                    current+=1

                if count>max_length:
                    max_length=count
        return max_length