// brute force idc
// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         // using 2 pointers
//         for (int i = 0; i < nums.size(); i++) {
//             for (int j = i + 1; j < nums.size(); j++) {
//                 if (nums[j] + nums[i] == target) {
//                     return {i, j};
//                 }
//             }
//         }
//         return {};
//     }
// };

// hashmap
class Solution {
    public: 
        vector<int> twoSum(vector<int>& nums, int target) {
            // unordered_map as that twat
            unordered_map<int, int> index;

            // put keyval in that -> forming a Python-like dictionary
            for (int i = 0; i < nums.size(); i++) {
                index[nums[i]] = i;
            }

            for (int i = 0; i < nums.size(); i++) {
                int diff = target - nums[i];
                if (index.count(diff) && index[diff] != i) { 
                    return {i, index[diff]};
                }
            }
            return {};
        }
};