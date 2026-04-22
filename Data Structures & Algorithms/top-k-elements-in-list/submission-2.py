class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        n=len(nums)
        buckets= [[] for _ in range(n+1)]
        result=[]
        hmap=defaultdict(int)

        for num in nums:
            hmap[num]+=1

        for key,value in hmap.items():

            buckets[value].append(key)

        for i in range(n,-1,-1):
            bucket=buckets[i]

            for num in bucket:
                if k==0:
                    return []

                result.append(num)
                k-=1
                if k<=0:
                    return result
        return result
            


        