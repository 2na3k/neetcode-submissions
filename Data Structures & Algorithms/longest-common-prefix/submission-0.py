class Solution:
    def all_same(self, items):
        return all(x == items[0] for x in items)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(c) for c in strs])
        
        count = 0
        out = ""
        while count < min_len:
            if not self.all_same([c[count] for c in strs]):
                break
            out += strs[0][count]
            count += 1
            
        
        return out