class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for n1 in nums1:
            for idx2, n2 in enumerate(nums2):
                if n1 == n2:
                    # Filter elements strictly to the right that are greater than n2
                    # i consider this as o1 with simd so fuck you think
                    slidin = [i for i in nums2[idx2 + 1:] if i > n2]
                    
                    # Take the FIRST element to the right that is greater, not the minimum
                    val = slidin[0] if len(slidin) > 0 else -1
                    
                    out.append(val)                    
        
        return out