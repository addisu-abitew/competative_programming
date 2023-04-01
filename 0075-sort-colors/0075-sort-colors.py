class Solution(object):
    def sortColors(self, nums):
        red,white,blue = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            elif nums[i] == 2:
                blue += 1
        for r in range(red):
            nums[r] = 0
        for w in range(red, red+white):
            nums[w] = 1
        for b in range(red+white, red+white+blue):
            nums[b] = 2