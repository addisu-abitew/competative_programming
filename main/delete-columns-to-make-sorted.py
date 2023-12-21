class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col = 0
        deleted = 0
        while col < len(strs[0]):
            prev = strs[0][col]
            row = 1
            while row < len(strs):
                if strs[row][col] < prev:
                    deleted += 1
                    break
                prev = strs[row][col]
                row += 1
            col += 1
        return deleted