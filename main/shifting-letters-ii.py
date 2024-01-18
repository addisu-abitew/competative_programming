class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        # mark the beginnig and end of each shift
        mark = [0]*(n+1)
        for shift in shifts:
            start, end, dxn = shift
            mark[start] += 1 if dxn == 1 else -1
            mark[end+1] += -1 if dxn == 1 else 1
        # calculate the prefix sum of mark to get total shift at each position
        for i in range(1, n):
            mark[i] += mark[i-1]
        # find final string after shifting
        shifted = ''
        for i in range(n):
            init = ord(s[i]) - ord('a')
            final = ord('a') + (init + mark[i]) % 26
            shifted += chr(final)
        return shifted