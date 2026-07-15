class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:


        values= self.store[key]
        lo=0
        hi=len(values)-1
        result=''

        while lo<=hi:

            mid=(lo+hi)//2
            stored_timestamp=values[mid][0]
            
            if stored_timestamp<=timestamp:
                result=values[mid][1]
                lo=mid+1
            else:
                hi=mid-1
        return result


        
