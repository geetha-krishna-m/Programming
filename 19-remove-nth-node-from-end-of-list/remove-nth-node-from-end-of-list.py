# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        child = None
        def traverse(root):
            nonlocal n,child
            if(root == None):
                return -1
            l = traverse(root.next) + 1
            if(l%n == 0 and l//n == 1):
                root.next = root.next.next
            return l 
        l = traverse(head)
        if(l==n-1):
            return head.next
        return head    