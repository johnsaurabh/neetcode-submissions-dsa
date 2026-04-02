class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)

        for num in nums:
            count[num]+=1

            n=len(nums)

        buckets=[[] for _ in range(n+1)]

        for num,freq in count.items():
            buckets[freq].append(num)

        print(buckets)
        result=[]
        for freq in range(n,0,-1):
            for num in buckets[freq]:
                result.append(num)

                if len(result)==k:
                    return result
        