class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_d = {}

        for i in nums:
            if f_d.get(i, None) is None:
                f_d[i] = 0
            f_d[i] += 1
        
        print(f_d.keys())

        print(f_d.values()) # frequency
        
        top_k_f = list(sorted(f_d.values(), reverse=True))[:k]

        return [key for key in f_d.keys() if f_d[key] in top_k_f]