class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq_map=defaultdict(int)
        
        for task in tasks:
            freq_map[task]+=1
        
        max_heap=[-count for count in freq_map.values()]
        heapq.heapify(max_heap)

        #
        time=0
        queue=deque()

        while max_heap or queue:
            time+=1
            if max_heap:
                count=heapq.heappop(max_heap)
                count+=1

                if count<0:
                    queue.append((count,time+n))
            if queue and queue[0][1]==time:
                heapq.heappush(max_heap, queue.popleft()[0]) 
                
                 # popleft is O(1)
        return time



        