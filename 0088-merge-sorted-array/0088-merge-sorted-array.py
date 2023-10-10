class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, 0
        res = []
        while l < m and r < n:
            if nums1[l] < nums2[r]:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1
        while l < m:
            res.append(nums1[l])
            l += 1
        while r < n:
            res.append(nums2[r])
            r += 1
        for i in range(m+n):
            nums1[i] = res[i]