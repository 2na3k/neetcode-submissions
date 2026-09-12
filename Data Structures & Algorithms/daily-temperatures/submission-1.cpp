// brute force whatever -> 
// class Solution {
// public:
//     vector<int> dailyTemperatures(vector<int>& temperatures) {
//         int n = temperatures.size();
//         vector<int> res(n); // pre-allocation for the space of vector
//         for (int i = 0; i < n; i++) {
//             int count = 1;
//             int j = i + 1;
//             while (j < n) {
//                 if (temperatures[i] < temperatures[j]) {
//                     break;
//                 }
//                 j++;
//                 count++;
//             }
//             count = (j == n) ? 0 : count; //tenary operation?
//             res[i] = count;
//         }
//         return res;
//     }
// };

// stack
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        stack<pair<int, int>> stack; //would be a pair (temp, index)

        for (int i = 0; i < temperatures.size(); i++) {
            int t = temperatures[i];
            while (!stack.empty() && t > stack.top().first) {
                pair<int, int> pair = stack.top();
                stack.pop();
                res[pair.second] = i - pair.second;
            }
            stack.push({t, i});
        }
        return res;
    }
};
