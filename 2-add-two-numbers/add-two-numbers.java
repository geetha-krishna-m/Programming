/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0,null);
        ListNode temp = res;
        int sums=0,c=0;
        while(l1!=null || l2!=null || c!=0){
            sums = c;
            if(l1!=null){
                sums += l1.val;
                l1 = l1.next;
            }
            if(l2!=null){
                sums += l2.val;
                l2 = l2.next;
            }
            res.next = new ListNode(sums%10,null);
            res = res.next;
            c = (int)(sums/10);
        }
        return temp.next;  
    }
}