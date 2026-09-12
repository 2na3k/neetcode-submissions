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

 // return this solution later

// class Solution {
// public:
//     ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
//         ListNode* cur1 = list1;
//         ListNode* cur2 = list2;

//         ListNode* out; // can i do that like this?
        
        
//         while (cur1 != nullptr && cur2 != nullptr) {
//             if (cur1 < cur2) {
//                 out->next = cur1;
//                 cur1 = cur1->next;
//             }
//             else {
//                 out->next=cur2;
//             }
//             out = out->next;
//         }

//         return out;
//     }
// };


class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(0);
        ListNode* node = &dummy;

        while (list1 && list2) {
            if (list1->val < list2->val) {
                node->next = list1;
                list1 = list1->next;
            } else {
                node->next = list2;
                list2 = list2->next;
            }
            node = node->next;
        }

        if (list1) {
            node->next = list1;
        } else {
            node->next = list2;
        }

        return dummy.next;
    }
};