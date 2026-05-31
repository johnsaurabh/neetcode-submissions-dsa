# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry=0
        dummy=ListNode(0)
        current=dummy

        while l1 or l2 or carry:
            val1= l1.val if l1 else 0
            val2=l2.val if l2 else 0

            num=val1+val2+carry

            digit=num%10
            carry=num//10

            current.next=ListNode(digit)
            current=current.next

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
        
        