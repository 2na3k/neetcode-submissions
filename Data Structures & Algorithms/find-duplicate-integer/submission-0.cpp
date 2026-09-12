
// bro you suppose not to sort this shit ya kno -> hashmap gonna solve that
// class Solution {
// public:
//     int findDuplicate(std::vector<int>& nums) {
//         sort(nums.begin(), nums.end());
//         for (int i = 0; i < nums.size() - 1; i++) {
//             if (nums[i] == nums[i + 1]) {
//                 return nums[i];
//             }
//         }
//         return -1;
//     }
// };



class Solution {
public:
    int findDuplicate(std::vector<int>& nums) {
        int slow = 0, fast = 0;
        
        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast) {
                break;
            }
        }

        int slow2 = 0;
        while (true) {
            slow = nums[slow];
            slow2 = nums[slow2];
            if (slow == slow2) {
                return slow;
            }
        }
    }
};