"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodemap={}

        if not head:
            return None

        current=head

        while current!= None:
            newNode=Node(current.val)
            nodemap[current]=newNode
            current=current.next

        for original, newnode in nodemap.items():
            if original.next:
                newnode.next= nodemap[original.next]
            if original.random:
                newnode.random=nodemap[original.random]

        return nodemap[head]

        