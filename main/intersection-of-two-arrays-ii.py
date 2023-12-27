class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1counter = Counter(nums1)
        for num in nums2:
            if nums1counter[num]:
                intersection.append(num)
                nums1counter[num] -= 1
        return intersection