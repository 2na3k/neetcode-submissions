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
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        // note: this is the default way to loop through the linked list
        vector<ListNode*> nodes;
        ListNode* cur = head;
        while (cur != nullptr) {
            nodes.push_back(cur);
            cur = cur->next;
        }

        // soo, default we have something that could be used

        int ridx = nodes.size() - n;

        if (ridx == 0) {
            return head->next;
        }
        nodes[ridx - 1]->next = nodes[ridx]->next;
        return head;
    }
};
