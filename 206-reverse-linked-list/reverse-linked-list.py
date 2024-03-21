# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        z,x = None,head
        while x:
            temp = x.next
            x.next = z
            z = x
            x = temp   
        return z