class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        arr = [0] * (n+1)
        cand = []
        for t in trust:
            if arr[t[1]] != -1:
                arr[t[1]] += 1
                if arr[t[1]] == n-1: cand.append(t[1])
            arr[t[0]] = -1
        if len(cand)>0:
            for c in cand:
                if arr[c] != -1: return c
        return -1