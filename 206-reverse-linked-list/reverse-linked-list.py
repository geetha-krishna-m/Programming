# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            print("AS")
            return head
        dummy = ListNode(0,head)
        curr = dummy.next
        temp = curr
        while(temp!=None):
            forw = curr.next
            curr.next = forw.next
            temp = curr.next
            forw.next = dummy.next
            dummy.next = forw
        return dummy.next