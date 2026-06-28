class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low=0
        mid=0
        high=len(nums)-1

        while mid<=high:

            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
                #do something
            elif nums[mid]==2:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
                
                #do something
            else:
                mid+=1
                #or maybe someting else?

                
