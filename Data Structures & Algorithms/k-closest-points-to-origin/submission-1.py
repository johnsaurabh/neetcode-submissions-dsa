from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        
        heap=[]
        result=[]

        for x,y in points:
            dist = (x-0)**2 +(y-0)**2
            heapq.heappush(heap,(dist,[x,y]))
        

        for i in range(k):
            dist,point=heapq.heappop(heap)
            result.append(point)

        return result

        