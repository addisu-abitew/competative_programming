class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        equal = []
        for num in nums:
            if num > pivot:
                more.append(num)
            elif num < pivot:
                less.append(num)
            else:
                equal.append(num)
        return less + equal + more