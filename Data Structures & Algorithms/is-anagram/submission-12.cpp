// class Solution {
// public:
//     bool isAnagram(string s, string t) {
//         if (s.length() != t.length()) {
//             return false;
//         }
//         sort(s.begin(), s.end());
//         sort(t.begin(), t.end());
//         return s == t;
//     }
// };



// using array

class Solution {
    public: 
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        vector<int> counter(26, 0);
        for (int i = 0; i < s.length(); i++) {
            counter[s[i] - 'a']++;
            counter[t[i] - 'a']--;
        }

        for (int val: counter) {
            if (val != 0) {
                return false;
            }
        }

        return true;
    }
};