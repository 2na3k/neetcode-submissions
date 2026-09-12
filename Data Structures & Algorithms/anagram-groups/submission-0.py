class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref_dict = {}

        for word in strs:
            if ref_dict.get(str(sorted(word)), None) is None:
                ref_dict[str(sorted(word))] = []
            ref_dict[str(sorted(word))].append(word)
        
        return ref_dict.values()