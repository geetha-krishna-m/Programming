# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        odd,even = head,head.next
        firstOdd,temp = odd,even
        head = head.next.next
        cnt = 0
        while(head):
            if(cnt%2):
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            cnt += 1
            head = head.next
        odd.next = temp
        even.next=None
        return firstOdd