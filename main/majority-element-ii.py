class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        freq = []
        for num in count:
            if count[num] > len(nums)//3:
                freq.append(num)
        return freq