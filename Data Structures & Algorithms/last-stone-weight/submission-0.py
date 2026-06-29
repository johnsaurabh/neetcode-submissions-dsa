class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap= [-s for s in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            x=heapq.heappop(heap)
            y=heapq.heappop(heap)
           
                #the idea is heap[-1] will probably be the largest element,
                #and do it twice to smash x and y( becomes largest after x is smashed)
            if x<y:
               
                heapq.heappush(heap,x-y)

            
        return -heap[0] if heap else 0
            
                
        