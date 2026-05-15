class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        lo=0
        hi= len(self.store[key])-1
        result=''

        while lo<=hi:
            mid= (lo+hi)//2
            if self.store[key][mid][1]<=timestamp:
                result=self.store[key][mid][0]
                lo=mid+1

            else:
                hi=mid-1
            
        return result


        
