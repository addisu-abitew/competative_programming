class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)//2):
            ans.extend([nums[i*2 + 1]] * nums[i*2])
        return ans