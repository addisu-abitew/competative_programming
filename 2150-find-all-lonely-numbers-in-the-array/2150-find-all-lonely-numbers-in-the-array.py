class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        lonely = []
        nums.sort()
        for i in range(len(nums)):
            flag = True
            # see backward
            if i > 0 and (nums[i] == nums[i-1] or nums[i] == nums[i-1] + 1):
                continue
            # see forward
            if i < len(nums)-1 and (nums[i] == nums[i+1] or nums[i] == nums[i+1] - 1):
                continue
            lonely.append(nums[i])
        return lonely