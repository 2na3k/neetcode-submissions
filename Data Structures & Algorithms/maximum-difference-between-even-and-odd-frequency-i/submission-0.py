class Solution:
    def maxDifference(self, s: str) -> int:
        counter = {}
        for c in s:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1

        counter_list = counter.values()
        max_odds = max([i for i in counter_list if i % 2 == 1])
        min_even = min([i for i in counter_list if i % 2 == 0])

        return max_odds - min_even
