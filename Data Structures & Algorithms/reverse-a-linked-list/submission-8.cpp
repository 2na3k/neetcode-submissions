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


// I really don't understand a shit what I was writting there
// class Solution {
// public:
//     ListNode* reverseList(ListNode* head) {
//         if (!head) {
//             return nullptr;
//         }

//         ListNode* newHead = head;
//         if (head->next) {
//             newHead = reverseList(head->next);
//             head->next->next = head;
//         }
//         head->next = nullptr;

//         return newHead;
//     }
// };


// iteration = putting a dummy things there
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head; // start that thing in the first pos
        
        while (curr) {  // while should be start with curr + curr = prev = nullptr then ok
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
};