class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap=defaultdict(int)
        heap=[]


        for num in nums:
            hmap[num]+=1

        for num,freq in hmap.items():
            heapq.heappush(heap,[freq,num])
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq,num in heap]

        
        