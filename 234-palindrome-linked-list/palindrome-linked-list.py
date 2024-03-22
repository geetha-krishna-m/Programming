# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        def reverse(fast):
            nonlocal slow
            if fast == None:
                return True
            res = reverse(fast.next)
            if(fast.val == slow.val):
                slow = slow.next
                return res and True
            else:
                slow = slow.next
                return res and False
        return reverse(head)
        