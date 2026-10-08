class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap=defaultdict(int)
        heap=[]

        for num in nums:
            hmap[num]+=1

        for val,freq in hmap.items():
            heapq.heappush(heap,[freq,val])

            if len(heap)>k:
                heapq.heappop(heap)
        return [val for freq,val in heap]


        