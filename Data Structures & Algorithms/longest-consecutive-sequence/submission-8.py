class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set()
        max_length=0

        for num in nums:
            numset.add(num)

        for num in nums:

            if num-1 not in numset:
                current=num+1
                length=1

                while current in numset:
                    current+=1
                    length+=1
                max_length=max(max_length,length)
        return max_length
        
                


            


        