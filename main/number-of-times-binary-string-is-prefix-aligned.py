class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_i = 0
        count = 0
        for cur_i, flip_i in enumerate(flips):
            max_i = max(max_i, flip_i)
            count += max_i == cur_i+1
        return count