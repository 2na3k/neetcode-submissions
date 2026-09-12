class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for s in strs:
            sortes = ''.join(sorted(s))
            out[sortes].append(s)
        return list(out.values())