# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        cnt = 0
        while fast:
            fast = fast.next
            cnt += 1
        cnt = cnt//2
        while cnt > 0:
            slow = slow.next
            cnt -= 1
        return slow
        