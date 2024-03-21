# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(x,y):
            if x is None or x.next is None:
                return x
            y = x
            x = x.next
            z = recurse(x,y)
            x.next = y
            y.next = None
            x = y
            return z
        return recurse(head,head)