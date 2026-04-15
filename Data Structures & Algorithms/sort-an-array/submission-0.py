class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums)<=1:
            return nums
        mid=len(nums)//2

        left= nums[:mid]
        right=nums[mid:]
        left_sorted=  self.sortArray(left)
        right_sorted= self.sortArray(right)

        return self.merge(left_sorted,right_sorted)

    
    def merge(self, left,right):

        i=0
        j=0
        result=[]
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i=i+1
            
            else :
                result.append(right[j])
                j=j+1
            
        while i<len(left):
            result.append(left[i])
            i+=1

        while j<len(right):
            result.append(right[j])
            j+=1

        return result
    
          




        