class Solution:
    def maxDifference(self, s: str) -> int:
        counter = {}
        for c in s:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1

        counter_list = counter.values()
        max_odds = max([i for i in counter_list if i % 2 == 1])

        # not sure: edge case: if no even counter => stupidly done
        min_even = min([i for i in counter_list if i % 2 == 0])

        return max_odds - min_even


class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        odd_max, even_min = 0, len(s)

        for cnt in counter.values():
            if cnt & 1:
                odd_max = max(odd_max, cnt)
            else:
                even_min = min(even_min, cnt)
        
        return odd_max - even_min