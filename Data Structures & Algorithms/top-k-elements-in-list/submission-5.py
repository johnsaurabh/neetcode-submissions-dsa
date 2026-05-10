class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n=len(nums)
        hmap=defaultdict(int)
        buckets= [[] for _ in range(n+1)]
        result=[]


        for num in nums:
            hmap[num]+=1

        for num, freq in hmap.items():
            buckets[freq].append(num)

        for i in range(n,-1,-1):
            bucket=buckets[i]
            for num in bucket:
                if k>0:
                    result.append(num)
                    k-=1
               
                
        return result



        