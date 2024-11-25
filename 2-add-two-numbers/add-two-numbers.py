# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        # def recurse(l1,l2):
        #     if(not l1 and not l2):
        #         return
        #     if(l1 and l2):
        #         recurse(l1.next,l2.next)
        #     elif(l1):
        #         recurse(l1.next,l2)
        #     elif(l2):
        #         recurse(l1,l2.next)
        sums,c = 0,0
        while(l1 or l2):
            if(l1):
                sums += l1.val
                l1 = l1.next
            if(l2):
                sums += l2.val
                l2 = l2.next
            temp.val = temp.val + sums
            c = temp.val//10
            if(not l1 and not l2 and c==0):
                continue
            temp.next = ListNode(c)
            temp.val = temp.val%10
            temp = temp.next
            sums = 0
        return dummy       