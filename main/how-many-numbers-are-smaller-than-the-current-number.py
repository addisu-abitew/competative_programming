class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        sorted_nums = sorted(nums)
        for i, n in enumerate(sorted_nums):
            if n not in dic:
                dic[n] = i
        ans = []
        for n in nums:
            ans.append(dic[n])
        return ans