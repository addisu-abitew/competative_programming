class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0: return False
        arr = []
        for num in nums:
            if num in arr:
                return True
            if len(arr) == k:
                arr.pop(0)
            arr.append(num)
        return False