class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head->next) return;
        
        // Find the middle of the list
        ListNode* middle = findMiddleOfList(head);
        
        // Reverse the second half of list
        ListNode* right = reverseList(middle->next);
        middle->next = nullptr;
        
        // Now, reorder the list
        ListNode *left = head, *currL = left, *currR = right;
        while(left && right) {
            currL = left;
            currR = right;
            left = left->next;
            right = right->next;
            currL->next = currR;
            currR->next = left;
        }
    }
    
private:
    ListNode* findMiddleOfList(ListNode* node) {
        ListNode *slow = node, *fast = node;
        
        while(fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
    }
    
    ListNode* reverseList(ListNode* node) {
        ListNode *curr = node, *upcoming = node, *prev = nullptr;
        while(curr->next) {
            upcoming = curr->next;
            curr->next = prev;
            prev = curr;
            curr = upcoming;
        }
        curr->next = prev;
        return curr;
    }
};