class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        result=[]
        n=len(nums)
        
        for i in range(k):

            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)
        
        result.append(nums[dq[0]])
       
        for i in range(k,n):

            left=i-k+1
            if dq[0]<left:
                dq.popleft()
                left=i
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)
            result.append(nums[dq[0]])
        return result

        