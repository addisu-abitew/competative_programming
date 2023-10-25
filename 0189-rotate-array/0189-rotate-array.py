class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        r = k%n
        nums.extend(nums[:n-r])
        for i in range(n-r):
            nums.pop(0)