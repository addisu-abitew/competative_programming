class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        nums.insert(0, float('-inf'))
        li = 0
        for i in range(len(nums)):
            if nums[i] < nums[li]:
                if modified:
                    return False
                else:
                    modified = True
                    if nums[i] >= nums[li-1]:
                        li = i
            else:
                li = i
        return True