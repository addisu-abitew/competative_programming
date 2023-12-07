class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
        expected = set([x for x in range(left, right+1)])
        for rang in ranges:
            given = set([x for x in range(rang[0], rang[1]+1)])
            covered.update(expected & given)
        return covered == expected