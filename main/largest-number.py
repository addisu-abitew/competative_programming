class Solution(object):
    def largestNumber(self, nums):
        # transform the int to str
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            
        # sort the string in decreasing order
        nums.sort(reverse = True)
        
        # correct some irregularities
        for i in range(1, len(nums)):
            pi = i - 1
            while pi>=0 and int(nums[pi]+nums[i]) < int(nums[i]+nums[pi]):
                nums[i],nums[pi] = nums[pi], nums[i]
                pi -= 1
                i -= 1
        return str(int(''.join(nums)))