class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap=[]
        num_freq=defaultdict(int)

        for num in nums:
            num_freq[num]+=1

        for num, freq in num_freq.items():
            heapq.heappush(heap,(freq,num))

            if len(heap)>k:
                heapq.heappop(heap)
        
        return [num for freq,num in heap]

    
      
            

