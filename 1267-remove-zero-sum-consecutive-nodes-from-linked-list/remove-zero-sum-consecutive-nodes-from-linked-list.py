# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0,head)
        prefixsum = 0
        d = dict()
        d[0] = newHead
        while head:
            prefixsum += head.val
            d[prefixsum] = head
            head = head.next
        head = newHead
        prefixsum = 0
        while head:
            prefixsum = prefixsum + head.val
            print(prefixsum)
            head.next = d[prefixsum].next
            head = head.next
        return newHead.next


        