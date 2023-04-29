from queue import PriorityQueue

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = []
        dec = []
        l = 0
        max_len = 0
        for i in range(len(nums)):
            while True:
                if len(inc) == 0:
                    inc.append(i)
                    break
                if nums[i] <= nums[inc[-1]]:
                    inc.pop()
                else:
                    inc.append(i)
                    break
            while True:
                if len(dec) == 0:
                    dec.append(i)
                    break
                if nums[i] >= nums[dec[-1]]:
                    dec.pop()
                else:
                    dec.append(i)
                    break
            # print(dec, inc)
            while True:
                if nums[dec[0]] - nums[inc[0]] > limit:
                    l += 1
                    if dec[0] < l:
                        dec.pop(0)
                    elif inc[0] < l:
                        inc.pop(0)
                else:
                    max_len = max(max_len, i-l+1)
                    break
        return max_len