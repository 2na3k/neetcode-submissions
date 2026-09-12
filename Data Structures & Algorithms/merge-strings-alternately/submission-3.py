class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        dummy = ""
        for i in range(min([len1, len2])):
            dummy += word1[i]
            dummy += word2[i]
        
        print(dummy)
        if len1 > len2:
            return dummy + word1[i+1:]
        elif len1 < len2:
            return dummy + word2[i+1:]
        else:
            return dummy