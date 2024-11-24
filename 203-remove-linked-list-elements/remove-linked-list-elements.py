# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode()
        final = res
        while(head):
            while(head and head.val ==val):
                head = head.next
            res.next = head
            res = res.next
            if(head):
                head = head.next
        return final.next