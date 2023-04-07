class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num1 in nums1:
            for i in range(nums2.index(num1)+1, len(nums2)):
                if nums2[i] > num1:
                    res.append(nums2[i])
                    break
            else:
                res.append(-1)
        return res