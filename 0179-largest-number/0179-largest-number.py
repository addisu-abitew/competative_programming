class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # transform the int to str
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        nums.sort(reverse = True)
        for i in range(1, len(nums)):
            pi = i - 1
            while pi>=0 and int(nums[pi]+nums[i]) < int(nums[i]+nums[pi]):
                nums[i],nums[pi] = nums[pi], nums[i]
                pi -= 1
                i -= 1
        return str(int(''.join(nums)))