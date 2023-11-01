class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = [0]
        for num in nums[:-1]:
            leftsum.append(leftsum[-1] + num)
        rightsum = [0]
        for num in nums[::-1][:-1]:
            rightsum.append(rightsum[-1] + num)
        rightsum.reverse()
        res = []
        for i in range(len(nums)):
            res.append(abs(leftsum[i]-rightsum[i]))
        return res