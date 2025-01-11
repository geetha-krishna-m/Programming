# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        for i in range(1,left):
            prev = prev.next
        curr = prev.next
        for i in range(right-left):
            store = curr.next
            curr.next = store.next
            store.next = prev.next
            prev.next = store
        return dummy.next
        