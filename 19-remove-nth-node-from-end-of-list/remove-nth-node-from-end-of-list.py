# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        cnt = 0
        while(temp):
            temp = temp.next
            cnt += 1
        if(n>cnt or not head):
            return head
        else:
            dummy = ListNode(0,head)
            res = dummy
            for i in range(cnt-n):
                res = res.next
            res.next = res.next.next
            return dummy.next

        