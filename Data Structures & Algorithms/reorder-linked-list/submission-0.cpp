/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        // there phases
        // first phase: find the mid point by slow-fast pointer
        ListNode* slow = head;
        ListNode* fast = head->next;
        
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* second = slow->next;

        // second phase: reverse the second half of the list
        ListNode* prev = slow->next = nullptr;
        while (second != nullptr) {
            ListNode* tmp = second->next;
            second->next = prev;
            prev = second;
            second = tmp;
        }

        // thrid phase: merge 2 half
        ListNode* first = head;
        second = prev;
        while (second != nullptr) {
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;
            first->next = second;
            second->next = tmp1;
            first = tmp1;
            second = tmp2;
        }
    }
};
