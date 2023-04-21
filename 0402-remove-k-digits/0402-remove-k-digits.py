class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        nums = list(num)
        removed = 0
        i ,p = 0 ,-1
        while i < len(nums):
            while i > 0 and nums[i] <= nums[p]:
                tmp = i
                while tmp < len(nums) and nums[tmp] == nums[p]:
                    tmp += 1
                
                if tmp == len(nums): 
                    nums = nums[:len(nums)-(k-removed)]
                    return str(int(''.join(nums)))
                elif nums[tmp] < nums[p]:
                    r = min(tmp-p, k-removed)
                    nums = nums[:p] + nums[p+r:]
                    removed += r
                    if removed == k:
                        return str(int(''.join(nums)))
                    i -= 1
                    p -=  1
                else:
                    i = tmp
                    p = i -1
                    break
            p = i
            i += 1
        nums = nums[:len(nums)-(k-removed)]
        return str(int(''.join(nums)))