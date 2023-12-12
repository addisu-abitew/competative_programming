class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        for num in count:
            if count[num] > len(arr)//4:
                return num