class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        l, r = 0, 0
        while l<len(nums1) and r<len(nums2):
            if nums1[l]<nums2[r]:
                merged.append(nums1[l])
                l += 1
            else:
                merged.append(nums2[r])
                r += 1
        if l<len(nums1): merged.extend(nums1[l:])
        if r<len(nums2): merged.extend(nums2[r:])
        
        n = len(merged)
        if n%2 == 1:
            return merged[n//2]
        else:
            return (merged[n//2]+merged[n//2-1])/2.0