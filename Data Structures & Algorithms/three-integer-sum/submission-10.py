class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result=[]


        for i in range(n-2):

            if i>0 and nums[i-1]==nums[i]:
                continue
            
            left=i+1
            right=n-1
            target=-nums[i]
            while left<right:
                s=nums[left]+nums[right]
                if s<target:
                    left+=1
                elif s>target:
                    right-=1
                
                else:
                    result.append([nums[i],nums[left],nums[right]])

                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[left]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return result


