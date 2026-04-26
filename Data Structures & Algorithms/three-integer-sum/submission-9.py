class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #For this solution to work, the array needs to be sorted.
        #This is a two pointer pattern problem.
        #I need a for loop to iterate through the main array, and a left pointer and a right pointer.
        #The trick is, if the sum of left pointer and right pointer is less than target, which is nums[i], 
        #then increment the left pointer, else increment the right pointer.
        #What are the edge cases or trip or gotachas I need to be aware of:
        # if nums[i] and i++ is the same then go past it. You will end up with the same triplet again. The triplets need to be unique
        # Ifin the inner loop, the left pointer or the right pointer are equal to the values next to them, skip past them.
        #Don't forget to increment the left and the right pointer.


        nums.sort()
        n=len(nums)
        result=[]

        

        for i in range(n-2):

            left=i+1
            right=n-1
          

            if i>0 and nums[i]==nums[i-1]:
                continue

           
            target=-nums[i]
            while left<right:

                s=nums[left]+nums[right]
                if s<target:
                    left+=1
                elif s> target:
                    right-=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                

                    left+=1
                    right-=1
        return result


            
                



