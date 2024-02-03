class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distincts = len(Counter(nums).keys())
        subarray = {}
        complete = 0
        left = 0
        for right in range(len(nums)):
            subarray[nums[right]] = subarray.get(nums[right], 0) + 1
            while len(subarray) == distincts:
                if subarray[nums[left]] == 1:
                    del subarray[nums[left]]
                else:
                    subarray[nums[left]] -= 1
                left += 1
            complete += left
        return complete