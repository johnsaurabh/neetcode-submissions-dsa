class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n=len(nums)
        buckets= [[] for _ in range(n+1)]
        freq_dict=defaultdict(int)
        result=[]
        if k==0:
            return result

        for num in nums:
            freq_dict[num]+=1
        
        for num,freq in freq_dict.items():
            
            buckets[freq].append(num)

        for i in range(n,-1,-1):
            
            bucket=buckets[i]
            for num in bucket:
                result.append(num)
                k-=1
                if k<=0:
                    return result
            
        return result
            



            

        
        