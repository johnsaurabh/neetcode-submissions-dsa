class MyHashMap:

    def __init__(self):
        self.size=1000
        self.buckets= [ [] for _ in range(self.size)]

        
    def put(self, key: int, value: int) -> None:

        index= key % self.size
        bucket= self.buckets[index]

        for pair in bucket:
            if pair[0]==key:
                pair[1]=value
                return
            
        bucket.append([key,value])
            

    def get(self, key: int) -> int:

        index= key % self.size
        bucket= self.buckets[index]

        for pair in bucket:
            if pair[0]==key:
                return pair[1]
        return -1
        

    def remove(self, key: int) -> None:
        
        index= key % self.size
        bucket= self.buckets[index]

        for i,pair in enumerate(bucket):

            if pair[0]==key:
                bucket.pop(i)
                return
        return


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)