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


// origin: brute force by just push everything into a thing
// class Solution {
// public:
//     ListNode* removeNthFromEnd(ListNode* head, int n) {

//         // note: this is the default way to loop through the linked list
//         vector<ListNode*> nodes;
//         ListNode* cur = head;
//         while (cur != nullptr) {
//             nodes.push_back(cur);
//             cur = cur->next;
//         }

//         // soo, default we have something that could be used

//         int ridx = nodes.size() - n;

//         if (ridx == 0) {
//             return head->next;
//         }
//         nodes[ridx - 1]->next = nodes[ridx]->next;
//         return head;
//     }
// };


// what
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int counter = 0;
        ListNode* cur = head;
        while (cur != nullptr) {
            counter++;
            cur=cur->next;
        } // to get the fucking only n??? fucking crazy

        int ridx = counter - n;
        
        if (ridx == 0) {
            return head->next;
        }
        // okay the differences between the one above to this one is we again traverse
        cur = head;
        
        for (int i = 0; i < counter - 1; i++) {
            if ((i+1)==ridx) {
                cur->next = cur->next->next;
                break;
            }
            cur = cur->next;
        }
        return head;
    }
};


