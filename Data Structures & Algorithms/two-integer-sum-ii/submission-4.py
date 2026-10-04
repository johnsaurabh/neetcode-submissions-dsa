class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        j=n-1
        while i<j:
            num=numbers[i]+numbers[j]
            if num>target:
                j-=1
            elif num<target:
                i+=1
            else:
                return [i+1,j+1]
        



        