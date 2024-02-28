class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* head = nullptr; 
        ListNode** cur = &head; // cursor
        
        while (list1 || list2) {
            if (list1 && (!list2 || list1->val < list2->val)) {
                *cur = list1; // Point current node to list1 node
                list1 = list1->next;
            } else if (list2) {
                *cur = list2; // Point current node to list2 node
                list2 = list2->next; 
            }
            cur = &(*cur)->next;
        }
        
        return head;
    }
};
