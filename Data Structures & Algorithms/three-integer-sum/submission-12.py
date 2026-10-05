class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n=len(nums)
        result=[]
        if not nums:
            return []
        for i in range(n-2):

            target=-nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue

            j=i+1
            k=n-1

            while j<k:
                s=nums[j]+nums[k]
                if s<target:
                    j+=1
                elif s>target:
                    k-=1
                else:
                    result.append([nums[i],nums[j],nums[k]])

                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
        return result

        