class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = smaller = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= smaller:
                smaller = num
            else:
                return True
        return False