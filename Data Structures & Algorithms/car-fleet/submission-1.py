class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack=[]
        fleet_count=0
        last_fleet_time=0

        cars= sorted(zip(position,speed),reverse=True)

        for pos,speed in cars:
            time= (target-pos)/speed

            if fleet_count==0:
                fleet_count+=1
                last_fleet_time=time

            elif fleet_count>0 and time>last_fleet_time:
                fleet_count+=1
                last_fleet_time=time
        return fleet_count         