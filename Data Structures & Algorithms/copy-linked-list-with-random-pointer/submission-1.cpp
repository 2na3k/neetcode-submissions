/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

// class Solution {
// public:
//     unordered_map<Node*, Node*> map;
//     Node* copyRandomList(Node* head) {
        

//         if (head == nullptr) {
//             return nullptr;
//         }
//         if (map.count(head)) {
//             return map[head];
//         }

//         Node* copy = new Node(head->val);
//         map[head] = copy;
//         copy->next = copyRandomList(head->next);
//         copy->random = map[head->random];
//         return copy; 
//     }
// };


class Solution {
public:
    unordered_map<Node*, Node*> map;
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> old_cache;

        // don't get that much -> how?
        old_cache[NULL] = NULL;

        // if i follow this then this will be a construction for new linked list
        Node* cur = head;

        while (cur != nullptr) {
            Node* copy = new Node(cur->val);
            old_cache[cur] = copy;
            cur = cur->next;
        }

        cur = head;
        while (cur != nullptr) {
            Node* copy = old_cache[cur];
            copy->next = old_cache[cur->next];
            copy->random = old_cache[cur->random];
            cur = cur->next;
        }

        return old_cache[head];
    }
};

