class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
       
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1

        lo=0
        hi=len(nums1)
        n=len(nums1) +len(nums2)
        half=(n+1)//2


        while lo<=hi:

            partition1= (lo+hi)//2
            partition2=half-partition1

            max_left1=  float("-inf") if partition1 == 0 else nums1[partition1-1]
            max_left2=  float("-inf") if partition2 == 0 else nums2[partition2-1]
            min_right1= float("inf") if partition1 == len(nums1) else nums1[partition1]
            min_right2= float ("inf") if partition2 == len(nums2) else nums2[partition2]
            
            if max_left1<=min_right2 and max_left2<=min_right1:
                max_left= max(max_left1,max_left2)
                min_right=min(min_right1,min_right2)
                

                if n%2==0:
                    median=(max_left + min_right)/2
                else:
                    median=max_left
                return median
            elif max_left1>min_right2:
                hi=partition1-1
            else:
                lo=partition1+1
        
        return median





        
