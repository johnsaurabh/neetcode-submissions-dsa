# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast=head
        slow=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        current=slow

        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node

        first=head
        second=prev

        while second and second.next:
            first_temp=first.next
            second_temp=second.next
            first.next=second
            second.next=first_temp
            first=first_temp
            second=second_temp

        



        