class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        cars= sorted(zip(position,speed),reverse=True)

        for pos, speed in cars:
             time_to_arrive= (target-pos)/speed

             if not stack:
                stack.append(time_to_arrive)
             elif stack and time_to_arrive>stack[-1]:
                stack.append(time_to_arrive)
        return len(stack)

        