class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = set()
        for n in nums:
            if n in visited: return True
            visited.add(n)
        return False